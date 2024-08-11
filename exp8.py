import cvzone
import cv2
from cvzone.ClassificationModule import Classifier
cap = cv2.VideoCapture(0)
myClassifier = Classifier('1','labels.txt')
fpsReader = cvzone.FPS()
while True:
 _, img = cap.read()
 predictions, index = myClassifier.getPrediction(img,scale=1)
 print(predictions, index)
 fps, img = fpsReader.update(img,pos=(450,50))
 print(fps)
 cv2.imshow("image",img)
 cv2.waitKey(1)
