import inspect
import json

iif = inspect.isfunction
igm = inspect.getmembers
ifas = inspect.formatargspec
igfas = inspect.getfullargspec

for f in igm(json, iif):
    print('def {}'.format(ifas(*igfas(f[1]))))