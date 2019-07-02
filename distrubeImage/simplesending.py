
def topla(sayi1,sayi2):
    return sayi1+sayi2



"""import rpyc
import cv2
import numpy as np

def ImageReturn(img,eyecascade):
    eyes=eyecascade.detectMultiScale(img,3,5)
    open_cv_image = np.array(img) 
    for (ex, ey, ew, eh) in eyes:
        print(str(ex)+":"+str(ey)+":"+str(ew)+":"+str(eh))
        cv2.rectangle(open_cv_image, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return img


conn=rpyc.classic.connect("localhost")
conn.execute('import cv2')
conn.execute('import numpy as np')
In=conn.teleport(ImageReturn)   

img=cv2.imread('/home/ozcan/Desktop/RPCRMI/distrubeImage/seinfeld.jpg')
eyecascade=cv2.CascadeClassifier('/home/ozcan/Desktop/RPCRMI/distrubeImage/haarcascade_eye.xml')
rtrnImg=In(img,eyecascade)
cv2.imshow('gelen resim',rtrnImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""