from sstr import sstr
import unittest


class TestSstr(unittest.TestCase):
    def test_sstr(self):
        s1 = sstr('abcde')
        self.assertEqual(s1 << 0, 'abcde')
        self.assertEqual(s1 >> 0, 'abcde')
        self.assertEqual(s1 << 2, 'cdeab')
        self.assertEqual(s1 >> 2, 'deabc')
        self.assertEqual(s1 >> 5, 'abcde')
        self.assertTrue((s1 >> 5) << 5, 'abcde')

if __name__ == '__main__':
    unittest.main()