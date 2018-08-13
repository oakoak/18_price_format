import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_on_leading_zeros(self):
        self.assertEqual(format_price("000123"), "123")

    def test_on_insignificant_zeros(self):
        self.assertEqual(format_price("1.23000"), "1.23")

    def test_on_incorrect_price(self):
        self.assertIsNotNone("1233sdccccc12333")

    def test_without_int_part(self):
        self.assertEqual(format_price(".444"), "0.444")


if __name__ == "__main__":
    unittest.main()
