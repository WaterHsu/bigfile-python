import threading
import time
from  Queue import Queue


queue = Queue(1000)

class FileReader(threading.Thread):
    def run(self):
        global queue 
        self.read()
    def read(self): 
        start = time.time()
        fileName = "E://access.29.log"
        
        with open(fileName, "r") as f:
            while True:
                lines = f.readlines(100)
                if not lines:
                    queue.put('end_uull_aa_end')
                    print "end"
                    break
                for line in lines:
                    queue.put(line)
        end = time.time()
        print "read end: using " + str(end - start)

class UrlDealer(threading.Thread):
    def run(self):
        global queue 
        self.deal()
    def deal(self):
        start = time.time()
        fileName = "E://out2.txt"
        dict = {}
        while True:
            line = queue.get()
            queue.task_done()
            if 'end_uull_aa_end' in line:
                print line 
                break
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
        fileWrite = open(fileName, 'w')
        temp = 0
        while temp < 20:
            fileWrite.write(str(dict[temp]) + '\r\n')
            temp += 1 
        fileWrite.close()
        end = time.time()
        print 'deal end using' + str(end - start)


def test():
    reader = FileReader()
    dealer = UrlDealer()
    reader.start()
    dealer.start()

if __name__ == '__main__':
    test()