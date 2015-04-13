"""
project_04_10.py will create 3 threads. Each one will have name starting
with "T" followed by sequence number from 1 to 3. When seconds thread is
running directory will be changed. This will affect all threads after.
Seems like such global changes are affecting all threads even that each
one of them should be running in its own namespace. Most likely this is
caused because of GIL.
"""

import threading
import os


def simulate(name):
    if int(name[-1]) == 2:
        print("CWD (before) for thread '{}' is '{}'".format(name, os.getcwd()))
        os.chdir("/")
        print("CWD (after) for thread '{}' is '{}'".format(name, os.getcwd()))
    else:
        print("CWD for thread '{}' is '{}'".format(name, os.getcwd()))

for tn in range(1, 4):
    t = threading.Thread(target=simulate, args=("T{}".format(tn),))
    t.start()
    t.join()