#!/usr/bin/python3
import unittest
from Prog1 import addn

class TestSum(unittest.TestCase):
    def test_list_int(self):
        x,y=0,0
        res = addn(x,y)
        self.assertEqual(res,0)

if __name__=="__main__":
    unittest.main()
