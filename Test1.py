#!/usr/bin/python3
import unittest
from addp import addn

class TestSum(unittest.Testcase):
    def test_list_int(self):
        x,y=0,0
        res = addn(x,y)
        self.assertEqual(res,0)
       
