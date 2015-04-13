""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log
from timeit import Timer
import numpy


def groffle_slow(mass, density):
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog/(i+1)
    return total


def groffle_faster(mass, density):
    return log(mass * density) * sum(list(1/i for i in range(1, 10001)))

mass = 2.5
density = 12.0

timer_slower = Timer("total = groffle_slow(mass, density)",
                     "from __main__ import groffle_slow, mass, density")
timer_faster = Timer("total = groffle_faster(mass, density)",
                     "from __main__ import groffle_faster, mass, density")
time_slower = timer_slower.timeit(number=1000)
time_faster = timer_faster.timeit(number=1000)

slower_output = numpy.float32(groffle_slow(mass, density))
faster_output = numpy.float32(groffle_faster(mass, density))
try:
    assert(slower_output == faster_output)
    print("Test 1: Equal output")
except:
    print("Test 1: Not equal output")
finally:
    print("Test 1: {} -vs- {}".format(slower_output, faster_output))

try:
    assert(time_slower > 3*time_faster)
    print("Test 2: New functions is more than 3 times faster!")
except:
    print("Test 2: New function is not faster enough")
finally:
    print("Test 2: {} -vs- {} (3 x {})"
          .format(time_slower, 3*time_faster, time_faster))