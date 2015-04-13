from timeit import timeit
from random import random

num = 1000001
lst = [random() for i in range(num)]
genex = [random() for i in range(num)]

t1 = timeit("list(lst)", "from __main__ import lst", number=1)
t2 = timeit("[i for i in lst]", "from __main__ import lst", number=1)
t3 = timeit("list(genex)", "from __main__ import genex", number=1)
t4 = timeit("[i for i in genex]", "from __main__ import genex", number=1)

print("list(lst) time is {}".format(t1))
print("[i for i in lst] time is {}".format(t2))
print("list(genex) time is {}".format(t3))
print("[i for i in genex] time is {}".format(t4))