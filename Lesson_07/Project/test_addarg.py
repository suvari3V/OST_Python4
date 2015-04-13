from addarg import addarg
import unittest


@addarg(1)
def prargs(*args):
    return args


@addarg(1)
def prkwargs(*args, **kwargs):
    return args, kwargs


class TestDecorator(unittest.TestCase):
    def test_addarg(self):
        self.assertEqual(prargs.__name__, "prargs")
        self.assertEqual(prargs(2, 3), (1, 2, 3))
        self.assertEqual(prargs("child"), (1, "child"))
        self.assertEqual(prkwargs(args_func="prargs", kwargs_func="prkwargs"),
                         ((1,), {"args_func": "prargs",
                                 "kwargs_func": "prkwargs"}))

if __name__ == '__main__':
    unittest.main()