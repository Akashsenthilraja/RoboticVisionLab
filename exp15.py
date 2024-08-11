import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
img = cv2.imread('eagle_grayscale.jpeg')
img_flatten = img.ravel()
plt.figure(figsize = [18, 5])

plt.subplot(131)
plt.imshow(img,cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.hist(img_flatten, 5, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('5 Bins')

plt.subplot(133)
plt.hist(img_flatten, 50, [0, 256])
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Numer of Pixels')
plt.title('50 Bins')
plt.show()
