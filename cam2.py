import cv2
import time
cam = cv2.VideoCapture(0) #0 for cam 1, i.e laptop's builtin cam
time.sleep(1)
ret, frame = cam.read()
if ret != True:
    raise ValueError("Can't read frame")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cam.png', gray)
cv2.imshow("cam", gray)
cv2.waitKey(1)
time.sleep(2)
