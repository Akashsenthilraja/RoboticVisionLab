import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('arithmetic.jpg')
matrix=np.ones(img.shape,dtype='uint8')*30
img_darker=cv2.subtract(img,matrix)
img_brighter=cv2.add(img,matrix)

plt.figure(figsize=[18,5])
plt.subplot(131)
plt.imshow(cv2.cvtColor(img_darker,cv2.COLOR_BGR2RGB))
plt.title("Darker")
plt.axis('off')


plt.subplot(132)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')


plt.subplot(133)
plt.imshow(cv2.cvtColor(img_brighter,cv2.COLOR_BGR2RGB))
plt.title("Brighter")
plt.axis('off')

plt.show()