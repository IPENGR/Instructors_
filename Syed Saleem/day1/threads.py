
from  threading import *
from time import  sleep



class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
  
  

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


a=hello()
b=hi()
a.start()
sleep(0.2)
b.start()
a.join()
b.join()

print("bye")