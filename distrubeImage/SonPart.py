#Stajda en son yazılan python kodu
import cv2
import rpyc
import numpy as np
from PIL import Image
import simplesending

def eyeResim2(img,faceCasc):
    npArray=np.array(img)
    faces= faceCasc.detectMultiScale(img,1.1,3)
    for(x,y,w,h) in faces:
        cv2.rectangle(npArray,(x,y),(x+w,y+h),(0,5,0),1)
    asd=np.asarray(npArray)
    print(asd)
    img=Image.fromarray(asd)
    return img


face_cascade = cv2.CascadeClassifier('/home/muhammet/Desktop/projePython/RPCImageSending/distrubeImage/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/muhammet/Desktop/projePython/RPCImageSending/distrubeImage/haarcascade_eye.xml')
img = cv2.imread('/home/muhammet/Desktop/projePython/RPCImageSending/distrubeImage/seinfeld.jpg')


conn=rpyc.classic.connect("localhost")
conn.execute('import cv2')
conn.execute('import numpy as np')
conn.execute('from PIL import Image')
conn.execute('print("merhaba")')
conn.execute('print("merhaba")')


In=conn.teleport(eyeResim2)
returnI=In(img,eye_cascade)
Image32=returnI
print(Image32)
Image32.show()


cv2.waitKey(0)
cv2.destroyAllWindows() 

