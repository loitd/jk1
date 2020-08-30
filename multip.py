'''
Created Date: Saturday August 22nd 2020
Author: Leo Tran (https://github.com/loitd)
-----
Last Modified: Saturday August 22nd 2020 11:16:21 pm
Modified By: Leo Tran (https://github.com/loitd)
-----
HISTORY:
Date      	By    	Comments
----------	------	---------------------------------------------------------
22-08-2020	loitd	Initialize the file
'''
from multiprocessing import Pool, Process, Queue, Pipe, Lock, Value, Array, Manager
import os
from lutils.utils import printlog

def func(d,l):
    printlog(d)
    printlog(l)

if __name__ == "__main__":
    # Functionality within this package requires that the __main__ module be importable by the children
    with Manager() as man:
        d = man.dict()
        l = man.list([1,2,3,4,5,6])
        with Pool(processes=3) as pool:
            res = [pool.apply_async(os.getpid,()) for i in l]
            printlog([i.get(timeout=100) for i in res])
        print("No more pool")