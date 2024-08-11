import cv2
import numpy as np
img=cv2.imread('eagle_grayscale.jpeg')
kernel=np.ones((5,5),np.uint8)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(17,17),0)
imgCanny=cv2.Canny(img,150,200)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow('Canny',imgCanny)
cv2.imshow('Dilation',imgDilation)
cv2.imshow('Blur',imgBlur)
cv2.imshow('Gray',imgGray)
cv2.waitKey(0)