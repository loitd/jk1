'''
Created Date: Sunday August 23rd 2020
Author: Leo Tran (https://github.com/loitd)
-----
Last Modified: Sunday August 23rd 2020 4:40:35 pm
Modified By: Leo Tran (https://github.com/loitd)
-----
HISTORY:
Date      	By    	Comments
----------	------	---------------------------------------------------------
23-08-2020	loitd	Initialize the file
'''
import threading
import time
from lutils.utils import printlog, printwait
import queue

EXITFLAG = 0
GRACEFULEXITFLAG = 0

ev = threading.Event()
cd = threading.Condition()
br = threading.Barrier(parties=2) #1 for controller, 1 for main thread
l = threading.Lock()
q = queue.Queue(1000)
s = threading.Semaphore(3)

def worker(i, l, q):
    printlog("worker {0} started".format(i))
    data = None
    while not EXITFLAG and not GRACEFULEXITFLAG:
        l.acquire()
        if not q.empty():
            data = q.get()
            l.release()
            printwait("{0}".format(data), 10)
        else:
            l.release()
            time.sleep(10)

def controller(l, q, ev, br):
    printlog("controller started")
    l.acquire()
    [q.put(i) for i in range(10) if not q.full()]
    l.release()
    # time.sleep(10)
    # ev.set() #set the flag using event
    i = br.wait() #set the flag using barrier
    printlog("controller stopped")
    
ts = [threading.Thread(target=worker, args=(i,l,q), daemon=True) for i in range(2)]

printlog("Fill the queue")
ctl = threading.Thread(target=controller, args=(l,q,ev,br), daemon=True)
ctl.start()

# block = ev.wait(10) #wait in 10 sec using event
# if block:
try:
    i = br.wait(5) #main thread will wait for controller because main finished its job sooner than controller. Wait 5s or raise threading.BrokenBarrierError exception
    for t in ts:
        t.start()
    
    printlog("Wait for queue to be executed")
    while not q.empty():
        percent = 100-q.qsize()*100/10
        printwait("Percent: {0}".format(percent),2)
        pass

except threading.BrokenBarrierError as e:
    printlog("Timeout starting up controller")
except Exception as e:
    print("Exception: ", e)

_ = input("Press any key for ExitFLAG:")
EXITFLAG = 1

ctl.join()
(t.join() for t in ts if t.is_alive()) #timeout in 3 secs
print("Exit")