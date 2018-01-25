#C:Python31python.exe
# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys

image = cv2.imread("penguin.jpg")
cv2.imshow("penguin",image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

img = cv2.imread("Koala.jpg")
'''讓視窗可自由縮放大小'''
cv2.namedWindow("Koala", cv2.WINDOW_NORMAL)
cv2.imshow("Koala", img)
cv2.waitKey(0)
'''關掉koala 視窗'''
cv2.destroyWindow("Koala") 


