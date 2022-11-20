#!/usr/bin/python3
import unittest
from Prog1 import addn

class TestSum(unittest.Testcase):
    def test_list_int(self):
        x,y=1,2
        res = addn(x,y)
        self.assertEqual(res,3)

if __name__=="__main__":
    unittest.main()
