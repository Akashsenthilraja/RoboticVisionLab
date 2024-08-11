import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('arithmetic.jpg')
matrix=np.ones(img.shape,dtype='uint8')*30
matrix1=np.ones(img.shape,dtype='uint8')*2
matrix2=np.ones(img.shape,dtype='uint8')*4

img_lower=cv2.multiply(img,matrix1)
img_higher=cv2.multiply(img,matrix2)

plt.figure(figsize=[18,5])
plt.subplot(131)
plt.imshow(cv2.cvtColor(img_lower,cv2.COLOR_BGR2RGB))
plt.title("Lower")
plt.axis('off')


plt.subplot(132)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')


plt.subplot(133)
plt.imshow(cv2.cvtColor(img_higher,cv2.COLOR_BGR2RGB))
plt.title("Higher")
plt.axis('off')

plt.show()