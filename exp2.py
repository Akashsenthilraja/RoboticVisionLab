import cv2
vid=cv2.VideoCapture('video_clip.mp4')
while True:
    success,img=vid.read()
    if not success:
        break
    cv2.imshow('output',img)
    if 0xFF == ord('q') & cv2.waitKey(1):
        break

