#portfolio_test.py

import unittest
import mul

class portfolioTest(unittest.TestCase):
    def test_mul(self):
        p=mul.mul(3,5)
        self.assertEqual(15, p)

if __name__=='__main__':
    unittest.main()