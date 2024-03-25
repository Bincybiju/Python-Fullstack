import unittest
from testcheck import *
class unittesting(unittest.TestCase):
    x=2
    y=5
    result=mult(x,y)
    def test1(self):
        self.assertEqual(self.result,self.x*self.y)
    def test2(self):
        self.assertTrue('xz'.islower())
if __name__=="__main__":
            unittest.main()