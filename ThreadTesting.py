import time
import threading

mutex = threading._RLock()
count = 0
class MyThread(threading.Thread):
    def run(self):
        global count
        time.sleep(1)
        if mutex.acquire():
            for i in range(100):
                count = count + 1
            print 'thread{} add 1,count is {} \n'.format(self.name,count)
            mutex.release()

def main():
    print 'start main threading'
    threads=[MyThread() for i in range(10)]
    for t in threads:
        t.start()
    # for t in threads:
    #     t.join(3)

    print 'end main threading'

if __name__=='__main__':
    main()
