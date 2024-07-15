# test.py

import unittest
from main import modulus

class TestModulus(unittest.TestCase):

    def test_modulus_success(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(20, 4), 0)
        self.assertEqual(modulus(100, 7), 2)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

if __name__ == '__main__':
    unittest.main()
