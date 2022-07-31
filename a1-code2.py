import unittest
import main

class TestCalc(unittest.TestCase):

    def test_greater(self):
        self.assertTrue(main.is_greater(2, 3))

    def test_smaller(self):
        self.assertTrue(main.is_smaller(1, 0))

    def test_equal(self):
        self.assertTrue(main.is_equal(1, 2))

    def test_type(self):
        self.assertEqual(main.get_type(9), int)

    def test_negative(self):
        self.assertTrue(main.less_than_zero(-4))

if __name__ == '__main__':
    unittest.main()
