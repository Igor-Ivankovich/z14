import unittest
from unittest import mock
from functions import other_function, some_function_other, foo


class TestMock(unittest.TestCase):
    def test_other_function(self):
        with mock.patch('functions.some_function_other'):
            with mock.patch('functions.some_function') as func:
                func.return_value = 20
                self.assertEqual(func.call_count, 0)
                self.assertEqual(other_function(), 42)
                self.assertEqual(func.call_count, 1)

                func.return_value = 21
                self.assertEqual(other_function(), 98)
                self.assertEqual(func.call_count, 2)

                self.assertEqual(other_function(34), 98)
                self.assertEqual(list(func.call_args), [(34,), {}])

    @mock.patch('functions.some_function')
    @mock.patch('functions.some_function_other')
    def test_other_function_1(self, other, func):
        func.return_value = 20
        self.assertEqual(func.call_count, 0)
        self.assertEqual(other_function(), 42)
        self.assertEqual(func.call_count, 1)

    def test_some_function(self):
        with mock.patch('random.randint') as func:
            func.return_value = 30
            number = some_function_other()
            self.assertEqual(number, 30)

            func.return_value = 666
            with self.assertRaises(Exception):
                some_function_other()

    def test_foo(self):
        with mock.patch('functions.some_function_other') as func:
            func.side_effect = Exception("Text")
            self.assertEqual(foo(), "error")


if __name__ == '__main__':
    unittest.main()
