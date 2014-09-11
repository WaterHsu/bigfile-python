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
                if '.com' in line:
                    str1 = line[(line.index(' - ') + 3 ): (line.index('[') - 1)]
                 
                    str2 = line[line.index('\"') : line.index('HTTP')]
                    if '/' in str2:
                        str2 = str2[str2.index('/') : len(str2)]
                    url = str1 + str2
                    if not '/do_not_delete/noc.gif' in url:
                        if not '/70/70' in url:
                            if not '/50/50' in url:
                                if '?' in url:
                                    url = url[0: url.index('?')]
                                if(dict.has_key(url)):
                                    ff = dict[url]
                                    dict[url] = ff + 1
                                else:
                                    dict[url] = 1
                       
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