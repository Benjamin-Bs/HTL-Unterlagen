import cv2
import numpy as np

bg_subtractor = cv2.createBackgroundSubtractorMOG2()


cap = cv2.VideoCapture('video.mp4')

scale_factor = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    fg_mask = bg_subtractor.apply(frame)

    fg_removed = cv2.bitwise_and(frame, frame, mask=fg_mask)

    cv2.imshow('Foreground', fg_removed)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
