import time


def read():
    start = time.time()
    fileName = "E://access.29.log"
    with open(fileName, "r") as f:
        for line in f:
            m = 1
            
    end = time.time()
    print end - start 
    
def read2():
    start = time.time()
    fileName = "E://access.29.log"
    with open(fileName, "r") as f:
        print "begin"
        
        while True:
            lines = f.readlines(100)
            
            if not lines:
                break    
            for line in lines:
                m = 2 
    
    end = time.time()
    print end - start
    
if __name__ == '__main__':
    read2()