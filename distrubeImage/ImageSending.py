import cv2
import rpyc
import numpy as np
from PIL import Image
from xml.dom import minidom



""" cap=cv2.VideoCapture(0)
    while True:
        output=cap.read()
        eyecascade=cv2.CascadeClassifier('haarcascade_eye.xml')
        eyes=eyecascade.detectMultiScale(output,3,5)
        for(x,y,w,h) in eyes:
            output=cv2.rectangle(output,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('eye recogonition', output)
        k=cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()

eyefunction()

Image=cv2.VideoCapture(0).read()

"""
def ImageMultiScale(face_cascade,gray):
    faces=face_cascade.detectMultiScale(gray,3,5)
    return faces



def ImageProcess(eye_cascade,img):
    open_cv_image=np.array(img) 
    eyes=eye_cascade.detectMultiScale(img,3,5)
    for (ex, ey, ew, eh) in eyes:
        print(str(ex)+":"+str(ey)+":"+str(ew)+":"+str(eh))
        cv2.rectangle(open_cv_image, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return img




conn=rpyc.classic.connect("localhost")
conn.execute('import cv2')
conn.execute('import numpy as np')





In=conn.teleport(ImageProcess)   

face_cascade = cv2.CascadeClassifier('/home/ozcan/Desktop/RPCRMI/distrubeImage/haarcascade_frontalface_default.xml')
img = cv2.imread('/home/ozcan/Desktop/RPCRMI/distrubeImage/seinfeld.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Img=In( cv2.CascadeClassifier('/home/ozcan/Desktop/RPCRMI/distrubeImage/haarcascade_eye.xml'),img)
cv2.imshow('eye finder',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()
