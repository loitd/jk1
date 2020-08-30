import collections as cl
import itertools as it
from random import randint
import timeit
# import sys
# print(sys.getrecursionlimit())

ls = [i for i in range(10000000)] #10.000.000
dt = {k:v for k,v in enumerate(ls)}
tp = tuple(i for i in range(10000000))
st = set(i for i in range(10000000))
fs = frozenset(i for i in range(10000000))
it = (i for i in range(10000000))

def doit(inp):
    # print("* TYPE: {0}".format(type(inp)))
    for el in inp:
        el += 1
    return inp

def hasin(inp):
    return 9999999 in inp

def lookup(inp):
    return inp[9999999]

def hasinlist2dict(inp):
    _dt = {v:k for k,v in enumerate(inp)}
    return 9999999 in _dt

def hasindval(d):
    # test check in by values instead of keys
    return 9999999 in d.values()
    
if __name__ == "__main__":
    print("-------------------------Traverse-----------------------------")
    # print("LIST: ", timeit.timeit('doit(ls)', number=5, globals=globals()))
    # print("DICT: ", timeit.timeit('doit(dt)', number=5, globals=globals()))
    # print("TUPL: ", timeit.timeit('doit(tp)', number=5, globals=globals()))
    # print("ITER: ", timeit.timeit('doit(it)', number=5, globals=globals())) #------WIN 1/2 time
    # print("SET : ", timeit.timeit('doit(st)', number=5, globals=globals()))
    # print("FSET: ", timeit.timeit('doit(fs)', number=5, globals=globals()))
    print("--------------------------hasin-------------------------------")
    print("LIST: ", timeit.timeit('hasin(ls)', number=10, globals=globals()))
    print("DICT: ", timeit.timeit('hasin(dt)', number=10, globals=globals())) #-------->WIN
    # print("DVAL: ", timeit.timeit('hasindval(dt)', number=10, globals=globals())) #---> only KEYS is hashed, values is NOT HASHED
    print("TUPL: ", timeit.timeit('hasin(tp)', number=10, globals=globals()))
    print("ITER: ", timeit.timeit('hasin(it)', number=10, globals=globals())) #--------->WIN
    print("SET : ", timeit.timeit('hasin(st)', number=10, globals=globals())) #--------->
    print("FSET: ", timeit.timeit('hasin(fs)', number=10, globals=globals())) #--------->
    # print("L2D : ", timeit.timeit('hasinlist2dict(ls)', number=10, globals=globals()), "---> w/h LIST to DICT converse") #---------> FAILED
    print("--------------------------Lookup-------------------------------")
    # print("LIST: ", timeit.timeit('lookup(ls)', number=10, globals=globals()))
    # print("DICT: ", timeit.timeit('lookup(dt)', number=10, globals=globals()))
    # print("TUPL: ", timeit.timeit('lookup(tp)', number=10, globals=globals()))
    print("--------------------------Others-------------------------------")
    print("LIST SUM: ", timeit.timeit('sum(ls)', number=10, globals=globals()))
    print("LIST MAX: ", timeit.timeit('max(ls)', number=10, globals=globals()))
    print("LS SORT1: ", timeit.timeit('sorted(ls)', number=10, globals=globals()))
    print("LS SORT2: ", timeit.timeit('ls.sort()', number=10, globals=globals()))