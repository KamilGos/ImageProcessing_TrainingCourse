import numpy as np
import cv2

bgr = np.uint8([[[0,255,0]]])
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print(hsv)