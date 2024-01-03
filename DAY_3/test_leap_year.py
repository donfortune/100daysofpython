import unittest
from leap_year import is_leap_year

class test_case(unittest.TestCase):
    def test_leap(self):
        self.assertTrue(is_leap_year(2020))
        
        self.assertFalse(is_leap_year(2021))

        self.assertFalse(is_leap_year(1900))

        self.assertTrue(is_leap_year(2000))

if __name__ == '__main__':
    unittest.main()