"""
worker.py: a sample worker process that receive input and
           through one Queue and routines output through another.
"""
from multiprocessing import Process
import sys


class WorkerThread(Process):
    def __init__(self, iq, oq, *args, **kwargs):
        """Initialize process and save queue references."""
        Process.__init__(self, *args, **kwargs)
        self.iq, self.oq = iq, oq

    def run(self):
        while True:
            work = self.iq.get()
            if work is None:
                self.oq.put(None)
                print("Worker", self.name, "done")
                self.iq.task_done()
                break
            i, c = work
            result = (i, self.process(c))  # this is the "work"
            self.oq.put(result)
            self.iq.task_done()
        sys.stdout.flush()

    def process(self, s):
        """This defines how the string is processed to produce a result."""
        return s.upper()