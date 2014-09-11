import threading 
import time 
import random
from Queue import Queue

queue = Queue()

class Producer(threading.Thread):
    def run(self):
        global queue
        self.produce() 
        
    def produce(self):
        start = time.time()
        fileName = "E://access.29.log"
        
        with open(fileName, "r") as f:
            while True:
                lines = f.readlines(10000)
                if not lines:
                 #   queue.put('ddfffnnneeennnnddd')
                    break
                for line in lines:
                    #queue.put(line)
                    print line
                    ff = 33;
                    
        end = time.time()
        print "read end: using " + str(end - start)

        

class Consumer(threading.Thread):   
    def run(self):
        global queue
        self.consume()
    
    def consume(self):
        start = time.time()
        while True:
            line = queue.get()
            if 'ddfffnnneeennnnddd' in line:
                break
          #  print line   
            
        end = time.time()
        print "consume end: using " + str(end - start)   
 
if __name__ == '__main__':
    Producer().start()
  #  Consumer().start()           
            