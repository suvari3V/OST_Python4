"""
control.py: Creates queues, starts output and worker processes,
            and pushes input into the output queue.
"""

from worker import WorkerThread
from output import OutThread
from multiprocessing import JoinableQueue
import string
import random


if __name__ == '__main__':
    WORKERS = 10

    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = JoinableQueue(maxsize=int(WORKERS*1.5))

    ot = OutThread(WORKERS, outq)
    ot.start()

    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = ''.join([random.choice(string.ascii_letters)
                        for i in range(1000)])
    # Feed the process pool with work units
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")