import time

def read():
    start = time.time();
    fileName = "E://access.29.log"
    with open(fileName, "r") as f:
        for line in f:
            m = 1;
            
    end = time.time()
    print end - start 
    
if __name__ == '__main__':
    read()