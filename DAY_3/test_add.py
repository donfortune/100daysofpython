import unittest
from add import add

class test_case(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 5), 6)
    def test_add2(self):
        self.assertEqual(add(1, 7), 6)
        
        

        


if __name__ == '__main__':
    unittest.main()