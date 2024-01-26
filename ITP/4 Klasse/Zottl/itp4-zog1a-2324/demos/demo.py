import cv2

cap = cv2.VideoCapture(0)

success, img = cap.read()

while success:
    cv2.imshow("Window", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
    success, img = cap.read()

cap.release()

cv2.destroyWindow("Window")