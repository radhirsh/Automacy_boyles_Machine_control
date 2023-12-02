import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
while(cap.isOpened()):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, gb = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)

    gb = cv2.bitwise_not(gb)

    contour,hier = cv2.findContours(gb,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        cv2.drawContours(gb,[cnt],0,255,-1)
    gray = cv2.bitwise_not(gb)

    cv2.drawContours(gray,contour,-1,(0,255,0),3)

    cv2.imshow('test', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()