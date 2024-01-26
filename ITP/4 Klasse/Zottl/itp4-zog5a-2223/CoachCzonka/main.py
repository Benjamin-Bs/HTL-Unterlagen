import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# VIDEO FEED
#cap = cv2.VideoCapture("/Users/lorenz/Desktop/4.mp4")
cap = cv2.VideoCapture(0)

isValid = True

# counter variables
counter_squat = 0
counter_pushup = 0

stage_squat = None
stage_pushup = None


# Calculate angle of bodyguard
def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            # Calculate angle
            angle_elbow = calculate_angle(shoulder, elbow, wrist)
            elbow_angle = 180 - angle_elbow

            angle_shoulder = calculate_angle(shoulder, elbow, wrist)
            shoulder_angle = 180 - angle_shoulder

            angle_knee = calculate_angle(hip, knee, ankle)
            knee_angle = 180 - angle_knee

            angle_hip = calculate_angle(shoulder, hip, knee)
            hip_angle = 180 - angle_hip

            if (landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].visibility > 0.8 or
                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility > 0.8):

                # Pushup counter logic
                if elbow_angle > 30 and shoulder_angle > 40:
                    stage_pushup = "down"
                if hip_angle > 100:
                    isValid = False
                # Wenn Liegestütz richtig - liege = true
                if elbow_angle < 30 and shoulder_angle < 40 and stage_pushup == 'down' and isValid == True:
                    stage_pushup = "up"
                    isValid = True
                    counter_pushup += 1
                print(counter_pushup)
                print(isValid)

            if (landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility > 0.8 or
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility > 0.8):
                # Squat counter logic
                if knee_angle < 60 and hip_angle < 70:
                    stage_squat = "down"
                if knee_angle > 60 and hip_angle > 70 and stage_squat == 'down':
                    stage_squat = "up"
                    counter_squat += 1
                    print(counter_squat)

        except:
            pass

        # Render squat counter
        # Squat status box
        cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

        # Squat data
        cv2.putText(image, 'Squats', (10, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_squat),
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Stage data
        cv2.putText(image, 'STAGE', (68, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage_squat,
                    (60, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        # Render pushup counter
        # Setup status box
        cv2.rectangle(image, (0,77), (225, 150), (245, 117, 16), -1)

        # Pushup data
        cv2.putText(image, 'Pushups', (5, 89),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_pushup),
                    (10, 137),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Stage data
        cv2.putText(image, 'STAGE', (75, 89),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage_pushup,
                    (60, 137),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()