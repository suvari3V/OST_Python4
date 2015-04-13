from mydict import MyDict
import unittest


class TestMyDict(unittest.TestCase):
    def test_existing_key(self):
        md = MyDict('default')
        md['k1'] = 1
        self.assertEqual(md['k1'], 1)

    def test_missing_key(self):
        md = MyDict('default')
        self.assertEqual(md['k2'], 'default')

if __name__ == '__main__':
    unittest.main()