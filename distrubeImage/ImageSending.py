import cv2
import rpyc
from PIL import Image


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


def ImageProcess(Image,xmlfile):
    
    while True:
        output=Image.read()
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return Image




conn=rpyc.classic.connect("localhost")
conn.execute("import cv2")


img = Image.open('.vscode/distrubeImage/seinfeld.jpg')
img.show()
In=conn.teleport(ImageProcess)
gelenImage=In(img)
cv2.imshow(gelenImage)
cv2.waitKey(1)
cv2.destroyAllWindows()