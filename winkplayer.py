import cv2
import numpy as np

url = "https://s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/variant.m3u8"

cap = cv2.VideoCapture(url)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
