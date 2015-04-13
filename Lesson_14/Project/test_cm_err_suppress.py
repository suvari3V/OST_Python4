from cm_err_suppress import cm_err_suppress
import unittest


class TestCtxmErrSuppress(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(Exception):
            with cm_err_suppress():
                raise Exception("This exception should be raised")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            with cm_err_suppress() as cm:
                raise TypeError('e')

    def test_value_error(self):
        with cm_err_suppress() as cm:
            raise ValueError("This exception should be suppresssed")

if __name__ == "__main__":
    unittest.main()