import unittest
from calcu import add_numbers


class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add_numbers(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
