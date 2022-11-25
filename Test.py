#!/usr/bin/python3
import unittest
from Prog1 import addn

class TestSum(unittest.TestCase):
    def test_list_int1(self):
        x,y=0,0
        res = addn(x,y)
        self.assertEqual(res,0)
    
    def test_list_int2(self):
        x,y=1,2
        res = addn(x,y)
        self.assertEqual(res,3)
        
    def test_list_int3(self):
        x,y=-0.5,1
        res = addn(x,y)
        self.assertEqual(res,0.5)
        
    def test_list_int4(self):
        x,y=1,-2
        res = addn(x,y)
        self.assertEqual(res,-1)
        
    def test_list_int5(self):
        x,y=-1.5,1
        res = addn(x,y)
        self.assertEqual(res,-0.5)

if __name__=="__main__":
    unittest.main()
