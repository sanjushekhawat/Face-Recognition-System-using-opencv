import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('C:/Users/sanju/python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recongnizer =cv2.face.LBPHFaceRecognizer_create()
recongnizer.read("reconizer/trainingdata.yml")
id=0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id,conf=recongnizer.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="Sanju"
        if(id==2):
            id="Ankit"
        if(id==3):
            id="suraj"
        if( id == 4 ):
             id = "pawan" ;
        cv2.putText(frame, str(id), (x, y + h), fontface, fontscale, fontcolor)
    cv2.imshow("Face",frame)
    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

