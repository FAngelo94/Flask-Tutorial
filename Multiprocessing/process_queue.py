from multiprocessing import Process, Queue

def f(q, name):
    print("f=",name)
    for i in range(1,50000000):
        pass
    q.put([42, None, name])

if __name__ == '__main__':
    q = Queue()
    for i in range(1,5):
        p = Process(target=f, args=(q,"thread "+str(i)))
        p.start()
        #print(q.get())    # prints "[42, None, 'hello']"
    print(q.get)