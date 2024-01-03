import unittest
from add import add

class test_case(unittest.TestCase):
    def test_add(self):
        self.assertTrue(add(1, 5), 6)

        


if __name__ == '__main__':
    unittest.main()