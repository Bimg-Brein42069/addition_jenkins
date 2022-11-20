#!/usr/bin/python3
import unittest
from Prog1 import addn

class TestSum(unittest.Testcase):
    def test_list_int(self):
        x,y=2,2.5
        res = addn(x,y)
        self.assertEqual(res,4.5)

if __name__=="__main__":
    unittest.main()
