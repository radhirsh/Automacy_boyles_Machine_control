import cv2
webcam=cv2.VideoCapture(0)
ret, frame = webcam.read()

print (ret)

webcam.release(0)

cv2.imshow("my image", frame)


cv2.waitKey(0)

cv2.destroyAllWindows()

