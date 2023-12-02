import numpy as np
import cv2
from matplotlib import pyplot as plt
img =cv2.imread(r"C:\Users\ELCOT\PycharmProjects\pythonProject2\opencv_frame_0.png",0)
kernel = np.ones((5,5), np.uint8)

# create a CLAHE object (Arguments are optional).

clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7,7))
cl1 = clahe.apply(img)
#apply adaptive threshold
cl2 = cv2.medianBlur(cl1, 5)
th1 = cv2.adaptiveThreshold(cl2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,2.55)
#apply otsu threshold
blur = cv2.GaussianBlur(cl1,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#removing noise
th2 = th1 & th3
#morphological transform
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)
#finding outlines via contouring process
image=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#print(contours)
hierarchy =cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#print("HIERARCHY:",hierarchy)
img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#for i in range(len(contours)):
#print(contours[1])
pt = (contours[0])
dst = cv2.drawContours(img1, pt, -1, (0,0,255), 3)
print(dst)
#printing the results onto the screen
cv2.imwrite("out.jpg", dst)
cv2.imwrite("dst.jpg",dst)