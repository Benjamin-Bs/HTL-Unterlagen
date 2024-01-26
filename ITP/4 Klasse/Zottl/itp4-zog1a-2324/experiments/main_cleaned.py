from time import time
from keras.models import load_model
from keras.preprocessing import image
import cv2
import mediapipe as mp
import numpy as np

# ! Sollen die Bilder gespeichert werden?
save = False

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

last_time_right = time()
last_time_left = time()

last_difference_right = 0
last_difference_left = 0

def process(frame):
    model_path = './Models/model_trained.h5'

    model = load_model(model_path)

    img = frame

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    result = True

    if prediction[0][0] > 0.9:
        result = False

    id = time()

    print(f"Prediction: {prediction[0][0]} ({result}) (ID: {id})")

    if save:
        print(f"Saving image {id}... (Frame)")

        name = f"./Images/{id}.png"

        cv2.imwrite(name, frame)

    color = (0, 255, 0) if result else (0, 0, 255)

    window = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), color, 10)

    if result:
        cv2.putText(window, "Schlapfen", (20, 50) , cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    else:
        cv2.putText(window, "Nix Schlapfen", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Result", window)

    if save:
        print(f"Saving image {id}... (Result)")

        name_result = f"./Images/{id}_result.png"

        cv2.imwrite(name_result, window)

def process_frame_right(frame, landmarks):
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]
    right_heel = landmarks[mp_pose.PoseLandmark.RIGHT_HEEL]
    right_foot_index = landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]

    distance = -(right_knee.y - right_ankle.y)

    min_x = min(right_heel.x, right_foot_index.x, right_ankle.x)
    max_x = max(right_heel.x, right_foot_index.x, right_ankle.x)
    min_y = min(right_heel.y, right_foot_index.y, right_ankle.y)
    max_y = max(right_heel.y, right_foot_index.y, right_ankle.y)

    min_x, max_x, min_y, max_y = frame.shape[1]*min_x, frame.shape[1]*max_x, frame.shape[0]*min_y, frame.shape[0]*max_y

    x_difference = max_x - min_x
    y_difference = max_y - min_y

    difference = x_difference - y_difference

    if difference > 0:
        min_y = min_y - difference / 2
        max_y = max_y + difference / 2
    else:
        min_x = min_x + difference / 2
        max_x = max_x - difference / 2

    min_x, max_x, min_y, max_y = int(min_x), int(max_x), int(min_y), int(max_y)

    x_difference = max_x - min_x
    y_difference = max_y - min_y

    difference = x_difference - y_difference

    if difference > 0:
        max_y = max_y + difference
    else:
        max_x = max_x - difference

    factor = 100

    zoom = int(factor * distance)

    min_x, max_x, min_y, max_y = min_x - zoom, max_x + zoom, min_y - zoom, max_y + zoom

    if min_x < 0 or min_y < 0 or max_x > frame.shape[1] or max_y > frame.shape[0]:
        return

    cut_frame = frame[min_y:max_y, min_x:max_x]

    resized_frame = cv2.resize(cut_frame, (256, 256))

    process(resized_frame)

def process_frame_left(frame, landmarks):
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
    left_heel = landmarks[mp_pose.PoseLandmark.LEFT_HEEL]
    left_foot_index = landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]

    distance = -(left_knee.y - left_ankle.y)

    min_x = min(left_heel.x, left_foot_index.x, left_ankle.x)
    max_x = max(left_heel.x, left_foot_index.x, left_ankle.x)
    min_y = min(left_heel.y, left_foot_index.y, left_ankle.y)
    max_y = max(left_heel.y, left_foot_index.y, left_ankle.y)

    min_x, max_x, min_y, max_y = frame.shape[1]*min_x, frame.shape[1]*max_x, frame.shape[0]*min_y, frame.shape[0]*max_y

    x_difference = max_x - min_x
    y_difference = max_y - min_y

    difference = x_difference - y_difference

    if difference > 0:
        min_y = min_y - difference / 2
        max_y = max_y + difference / 2
    else:
        min_x = min_x + difference / 2
        max_x = max_x - difference / 2

    min_x, max_x, min_y, max_y = int(min_x), int(max_x), int(min_y), int(max_y)

    x_difference = max_x - min_x
    y_difference = max_y - min_y

    difference = x_difference - y_difference

    if difference > 0:
        max_y = max_y + difference
    else:
        max_x = max_x - difference

    factor = 100

    zoom = int(factor * distance)

    min_x, max_x, min_y, max_y = min_x - zoom, max_x + zoom, min_y - zoom, max_y + zoom

    if min_x < 0 or min_y < 0 or max_x > frame.shape[1] or max_y > frame.shape[0]:
        return

    cut_frame = frame[min_y:max_y, min_x:max_x]

    resized_frame = cv2.resize(cut_frame, (256, 256))

    process(resized_frame)

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
            last_time_right = time_now

            process_frame_right(frame, landmarks)

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

            last_time_left = time_now

            process_frame_left(frame, landmarks)
   
    last_difference_left = difference

def main():
    with (mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose):
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            # Skalieren des Bildes
            # frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

            # Pose Detection
            results = pose.process(frame)

            # Hintergrund analysieren und "entfernen"

            mask = bg_subtractor.apply(frame)

            result = cv2.bitwise_and(frame, frame, mask=mask)

            # Umwandeln des Bildes in RGB
            # result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(result, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # Rechter Fuß

                right_foot = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

                right_foot_visible = check_foot(right_foot)

                if right_foot_visible:
                    foot_detected_right(frame, results.pose_landmarks.landmark)

                # Linker Fuß
                
                left_foot = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]

                left_foot_visible = check_foot(left_foot)

                if left_foot_visible:
                    foot_detected_left(frame, results.pose_landmarks.landmark)

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