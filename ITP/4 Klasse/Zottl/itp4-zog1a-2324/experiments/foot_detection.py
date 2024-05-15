from time import time
import os
import cv2
import mediapipe as mp

# * Koordinaten der Füße in % der Bildschirmgröße

# Landmarks - Punkte auf dem Körper
# https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/

# Kümmert sich um das Zeichnen der Landmarks
mp_drawing = mp.solutions.drawing_utils

# Kümmert sich um die Detection der Landmarks
mp_pose = mp.solutions.pose

# Hintergrundsubtraktion
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# ? Hintergrundsubtraktion Parameter
# bg_subtractor.setBackgroundRatio(0.8)
# bg_subtractor.setDetectShadows(False)
# bg_subtractor.setHistory(80)
bg_subtractor.setShadowValue(0)
# bg_subtractor.setVarThreshold(50)

# Video Capture
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video.mp4')

# Auflösung des Videos anpassen
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cap.set(cv2.CAP_PROP_FPS, 30)

# Hier wird das Window initialisiert
cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
cv2.namedWindow("Window: Result", cv2.WINDOW_NORMAL)

# Methode, die prüft, ob EIN Fuß erkannt wurde
def check_foot(foot):
    # .visibility gibt an, wie sicher sich das Modell ist, dass es sich um den Fuß handelt
    # 0.0 = nicht sicher, 1.0 = sicher

    # Threshold, ab wann ein Fuß als erkannt gilt
    confidence_threshold = 0.8

    # Boolean, ob der Fuß erkannt wurde
    foot_visible = foot.visibility > confidence_threshold

    if foot_visible:
        return True  # Fuß wurde erkannt
    else:
        return False  # Fuß wurde nicht erkannt

def process_frame(frame, foot):
    print("Right Foot detected")
    print("Foot Coordinates:", foot)

    # Define the coordinates of the right foot landmarks
    right_heel, right_foot_index, right_ankle = foot

    # Print the landmark coordinates
    print("Right Heel:", right_heel)
    print("Right Foot Index:", right_foot_index)
    print("Right Ankle:", right_ankle)

    # Calculate the bounding box around the right foot landmarks
    min_x = min(right_heel.x, right_foot_index.x, right_ankle.x)
    max_x = max(right_heel.x, right_foot_index.x, right_ankle.x)
    min_y = min(right_heel.y, right_foot_index.y, right_ankle.y)
    max_y = max(right_heel.y, right_foot_index.y, right_ankle.y)

    # Convert bounding box coordinates to integers
    min_x, max_x, min_y, max_y = frame.shape[1]*min_x, frame.shape[1]*max_x, frame.shape[0]*min_y, frame.shape[0]*max_y

    # Check if the bounding box is valid (not empty)
    if min_x < max_x and min_y < max_y:
        min_x, max_x, min_y, max_y = int(min_x), int(max_x), int(min_y), int(max_y)

        # Crop the frame to focus on the right foot region
        right_foot_region = frame[min_y:max_y, min_x:max_x]

        # Check if the cropped region is valid (not empty)
        if not right_foot_region.size == 0:
            # Resize the cropped region to make it smaller (10% reduction)
            resize_factor = 1.1
            resized_right_foot = cv2.resize(right_foot_region, None, fx=resize_factor, fy=resize_factor)

            # Save the resized right foot image to a file
            cv2.imwrite(fileName("./DetectedFoot"), resized_right_foot)

            # Optionally, display the resized right foot image (remove if not needed)
            cv2.imshow('Resized Right Foot', resized_right_foot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Cropped region is empty.")
    else:
        print("Bounding box is empty.")


# Example usage
# Assuming you have a 'results' object containing pose landmarks
# right_foot_landmarks = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL],
#                          results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX],
#                          results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]]
# process_frame(frame, right_foot_landmarks, 'output_smaller_right_foot.jpg')

def fileName(path):
    # Get the path to the "Pictures" directory
    pictures_directory = os.path.expanduser(path)

    # Find the latest numbered foot image in the directory
    if is_folder_empty(pictures_directory):
        latest_number = 0
    else:
        for filename in os.listdir(pictures_directory):
            if filename.startswith('foot') and filename.endswith('.jpg'):
                try:
                    number = int(filename.replace('foot', '').replace('.jpg', ''))
                    if number > latest_number:
                        latest_number = number
                except ValueError:
                    pass

    # Determine the next available number
    next_number = latest_number + 1

    # Create the filename for the new foot image
    return os.path.join(pictures_directory, f'foot{next_number}.jpg')


def is_folder_empty(folder_path):
    try:
        # List all files and directories in the given folder
        items = os.listdir(folder_path)

        # Filter out directories and hidden files/folders
        items = [item for item in items if
                 not os.path.isdir(os.path.join(folder_path, item)) and not item.startswith('.')]

        # Check if the filtered list is empty
        return len(items) == 0
    except FileNotFoundError:
        # Handle the case where the folder doesn't exist
        return True

last_time_right = time()
last_time_left = time()

last_difference_right = 0
last_difference_left = 0

def foot_detected_right(frame, landmarks):
    right_heel = landmarks[mp_pose.PoseLandmark.RIGHT_HEEL]
    right_foot_index = landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]

    difference = right_heel.y - right_foot_index.y

    global last_difference_right

    did_something = False

    # Absetzen des Fußes
    if difference < 0 and last_difference_right > 0:
        time_now = time()

        global last_time_right

        if time_now - last_time_right > 1:
            print("Rechts")

            last_time_right = time_now
            
            did_something = True

            cv2.imshow("Image", frame)

        do_nothing = 0

    # Abheben des Fußes
    if difference > 0 and last_difference_right < 0:
        # print("Rechts: Fuß oben")
        do_nothing = 0

    last_difference_right = difference

def foot_detected_left(frame, landmarks):
    left_heel = landmarks[mp_pose.PoseLandmark.LEFT_HEEL]
    left_foot_index = landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]

    difference = left_heel.y - left_foot_index.y

    global last_difference_left

    # Absetzen des Fußes
    if difference < 0 and last_difference_left > 0:
        time_now = time()

        global last_time_left

        if time_now - last_time_left > 1:
            print("Links")

            last_time_left = time_now
            
            did_something = True

        do_nothing = 0

    # Abheben des Fußes
    if difference > 0 and last_difference_left < 0:
        # print("Links: Fuß oben")
        do_nothing = 0
        
    last_difference_left = difference

def main():
    with (mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose):
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            # Skalieren des Bildes
            frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

            # Pose Detection
            results = pose.process(frame)

            # Hintergrund analysieren und "entfernen"

            mask = bg_subtractor.apply(frame)

            result = cv2.bitwise_and(frame, frame, mask=mask)

            # Umwandeln des Bildes in RGB
            # result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # Rechter Fuß
                right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
                right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
                right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
                right_foot = [right_heel, right_foot_index, right_ankle]

                right_foot = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

                right_foot_visible = check_foot(right_foot)

                if right_foot_visible:
                    foot_detected_right(result, results.pose_landmarks.landmark)

                    # cv2.imwrite("right_foot.jpg", frame)

                    # cv2.imshow("Rechts", frame)
                    do_nothing = 0

                # Linker Fuß
                left_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL]
                left_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
                left_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
                left_foot = [left_heel, left_foot_index, left_ankle]

                #if foot_detected(left_heel):
                    #process_frame(frame, left_foot)

                left_foot_visible = check_foot(left_foot)

                if left_foot_visible:
                    foot_detected_left(result, results.pose_landmarks.landmark)

                    # cv2.imwrite("left_foot.jpg", frame)

                    # cv2.imshow("Links", frame)
                    do_nothing = 0

            # Window anzeigen
            cv2.imshow("Window", frame)
            cv2.imshow("Window: Result", result)

            # ESC zum Beenden
            if cv2.waitKey(10) & 0xFF == 27:
                break

    # Ressourcen freigeben

    cap.release()

    cv2.destroyWindow("Window")

# Main Methode
if __name__ == "__main__":
    main()