
import threading
import time

def fun1():
  while(True):
    time.sleep(1)
    print("ali")
   
def fun2():
    while(True):
        time.sleep(2)
        print("merhaba")
        

    
thread1 = threading.Thread(target = fun1)
thread1.start()
thread2 = threading.Thread(target = fun2)
thread2.start()
