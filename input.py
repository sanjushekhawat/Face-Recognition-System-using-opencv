
import cv2
face_classifier = cv2.CascadeClassifier('C:/Users/sanju/python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
id=input('Enter user id')
sample=0
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sample = sample + 1
        cv2.imwrite("Dataset/user." + str(id) + "." + str(sample) + ".jpg",gray[y:y+h,x:x+w] )
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    if (sample>100):
        break

cap.release()
cv2.destroyAllWindows()
