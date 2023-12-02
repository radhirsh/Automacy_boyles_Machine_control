import qr
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


image = cv2.imread(r"C:\Users\ELCOT\PycharmProjects\pythonProject2\patient details.png")

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")

cv2.imshow("QR Scanner", image)
cv2.waitKey(0)

import Anesthesia
