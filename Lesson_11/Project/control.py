"""
control.py: Creates queues, starts output and worker threads,
            and pushes input into the output queue.
"""

from worker import WorkerThread
from output import OutThread
from queue import Queue
from time import time
import string
import random

start_time = time()
WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
instring = ''.join([random.choice(string.ascii_letters) for i in range(1000)])
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
exec_time = time() - start_time
print("Execution time: {}".format(exec_time))
print("Control thread terminating")