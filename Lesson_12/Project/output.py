"""
output.py: The output process for the miniature framework.
"""
import multiprocessing
import sys

identity = lambda x: x


class OutThread(multiprocessing.Process):
    def __init__(self, N, q, sorting=True, *args, **kwargs):
        """Initialize process and save queue reference."""
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []

    def run(self):
        """Extract items from the output queue and print all until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
        print("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output)))
        print("Output process terminating")
        print("Final string is {} characters long".format(len(self.output)))
        sys.stdout.flush()