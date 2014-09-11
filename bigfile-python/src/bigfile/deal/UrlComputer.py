import time
from test.test_codecs import Str2StrTest
from audioop import reverse


def read2():
    start = time.time()
    fileName = "E://access.29.log"
    fileName2 = "E://out2.txt"
    dict = {}
    with open(fileName, "r") as f:
        print "begin"
        
        while True:
            lines = f.readlines(100)
            
            if not lines:
                break    
            for line in lines:
                if 'http://' in line:
                    str1 = line[line.index('http://') : len(line)] 
                    str2 = str1[0 : str1.index('\"')]
                    if '?' in str2:
                        str2 = str2[0 : str2.index('?')]
                    if dict.has_key(str2):
                        ff = dict[str2]
                        dict[str2] = ff + 1
                    else:
                        dict[str2] = 1
                        
                       
    dict = sorted(dict.iteritems(), key=lambda d:d[1], reverse = True)
    fileWrite = open(fileName2, 'w')
    temp = 0
    while temp < 20:
       fileWrite.write(str(dict[temp]) + '\r\n')
       temp += 1 
    fileWrite.close()
    end = time.time()
    print end - start

if __name__ == '__main__':
    read2()