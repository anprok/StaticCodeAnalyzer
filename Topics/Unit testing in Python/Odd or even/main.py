# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):
    even_test = 2
    odd_test = 1

    def test_when_output_true(self):
        self.assertTrue(is_even(self.even_test))

    def test_when_output_false(self):
        self.assertFalse(is_even(self.odd_test))


if __name__ == '__main__':
    unittest.main()