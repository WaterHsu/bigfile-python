import time


def read():
    start = time.time()
    fileName = "E://access-demo.log"
    with open(fileName, "r") as f:
        for line in f:
            m = 1
            
    end = time.time()
    print end - start 
    
def read2():
    start = time.time()
    fileName = "E://access-demo.log"
    with open(fileName, "r") as f:
        lines = f.readlines(100000)
        
        for line in lines:
            m = 1
            
    end = time.time()
    print end - start
    
if __name__ == '__main__':
    read2()