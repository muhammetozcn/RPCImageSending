import cv2
import rpyc
import numpy as np
from PIL import Image
import simplesending

def eyeResim(img,eye_cascade,face_cascade):
   
    opencvImage=np.array(img)

    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    gray = np.array(gray, dtype='uint8')
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = opencvImage[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(img)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    print('helloworld')
    return img


def eyeResim2(img,faceCasc):
    npArray=np.array(img)
    faces= faceCasc.detectMultiScale(img,1.1,3)
    for(x,y,w,h) in faces:
        cv2.rectangle(npArray,(x,y),(x+w,y+h),(0,255,0),2)
    asd=np.asarray(npArray)
    print(asd)
    img=Image.fromarray(asd)
    return img


face_cascade = cv2.CascadeClassifier('/home/ozcan/Desktop/RPCRMI/distrubeImage/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/ozcan/Desktop/RPCRMI/distrubeImage/haarcascade_eye.xml')
img = cv2.imread('/home/ozcan/Desktop/RPCRMI/distrubeImage/seinfeld.jpg')
"""
rtnr=eyeResim(img,eye_cascade,face_cascade)
cv2.imshow('gelenresimcik',rtnr)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

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

"""
In=conn.teleport(eyeResim)





rtrnImg=In(img,eye_cascade,face_cascade)

cv2.imshow('gelen resim',rtrnImg)
cv2.waitKey(0)
cv2.destroyAllWindows()   
"""