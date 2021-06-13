

import matplotlib.pyplot as plt
import cv2
import datetime
import subprocess

cascade_file="haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

now = datetime.datetime.now()

img = cv2.imread("picture/"+now.strftime('%m.%d.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale/"+now.strftime('%m/%d.gray.jpg'), img_gray)

face_list = cascade.detectMultiScale(img_gray, minSize=(150,150))

if len(face_list) == 0:
    print("失敗")
    import tweet
    quit()
    
for (x,y,w,h) in face_list:
    print("顔の座標(x,y,w,h):", x, y, w, h)
    red=(0,0,255)
    cv2.rectangle(img, (x,y), (x+w, y+h), red, thickness=20)
 
