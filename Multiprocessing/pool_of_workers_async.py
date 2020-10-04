from multiprocessing import Pool, TimeoutError
import time
import os

def f(x, pid=0):
    print("Thread ",x, "parent process", pid, "pid child", os.getpid())
    for i in range(1,100000000):
        pass
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=2) as pool:

        # evaluate "f(20)" asynchronously
        for i in range(1,20):
            pool.apply_async(f, (i,os.getpid()))      # runs in *only* one process
        pool.close()
        pool.join()
        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")

    p = Pool(processes=4)   
    # evaluate "f(20)" asynchronously
    for i in range(20, 30):
        p.apply_async(f, (i,os.getpid()))      # runs in *only* one process
    p.close()
    p.join()

    print("end")