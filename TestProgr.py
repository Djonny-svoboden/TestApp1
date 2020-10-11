import unittest as ut
import numpy as np
import Bruh as pt

class CalcTest(ut.TestCase):
    def test_add(self):
        self.assertEqual(pt.MyClass.Return_k(1,2,3,pt.MyClass.Progression(1,2,3),2),6)
    def test_add1(self):
        self.assertEqual(pt.MyClass.presenceElement
                         (2,pt.MyClass.Progression(1,2,3)),True)
    def test_add2(self):
        self.assertEqual(pt.MyClass.elemReturn
                         (0,pt.MyClass.Progression(1,2,3)),2)
        
if __name__ == '__main__':
    ut.main()

