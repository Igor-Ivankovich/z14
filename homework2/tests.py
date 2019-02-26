import unittest
from homework import custom_range, max_number


class CustomRangeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class')

    def setUp(self):
        print('object')

    def test_empty(self):
        self.assertEqual(custom_range(1, 1, 2), [])

    def test_not_empty(self):
        self.assertEqual(custom_range(1, 4, 2), [1, 3])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class MaxNumberTest(unittest.TestCase):

    def test_max_number(self):
        self.assertEqual(max_number(1, 5, 4), 5)
        self.assertEqual(max_number(1, 5, 6), 6)
        self.assertEqual(max_number(7, 5, 6), 7)


if __name__ == '__main__':
    unittest.main()
