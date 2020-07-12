import multiprocessing
import time


def fn(a, b):
    while True:
        print("vals=", a, b)
        time.sleep(2)


proc1 = multiprocessing.Process(target=fn, args=(1, 2))
proc2 = multiprocessing.Process(target=fn, args=(3, 4))
proc1.start()
proc2.start()
while True:
    print("t")
    time.sleep(3)