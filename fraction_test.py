import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_init(self):
        f = Fraction(5,2)
        self.assertEqual(5,f.numerator)
        self.assertEqual(2,f.denominator)    
        f= Fraction(2)
        self.assertEqual(2,f.numerator)
        self.assertEqual(1,f.denominator)
        f = Fraction(-3,8)
        self.assertEqual(-3,f.numerator)
        self.assertEqual(8,f.denominator)        

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12) + Fraction(2,3))
        self.assertEqual(Fraction(70,72),Fraction(6,8) + Fraction(2,9))
        self.assertEqual(Fraction(1),Fraction(1,3) + Fraction(2,3)) 
        self.assertEqual(Fraction(1),Fraction(7,10) + Fraction(3,10)) #float + float number

    def test_fraction_with_denominator_is_empty_list(self):
        #test wrong type
        with self.assertRaises(TypeError): 
            frac = Fraction(5,[])

    def test_fraction_with_numerator_is_str(self):
        #test wrong type
        with self.assertRaises(TypeError):
            frac = Fraction("aaa",6)   

    def test_zero_over_zero(self):
        # test ValueError 0/0
        with self.assertRaises(ValueError):
            frac = Fraction(0,0)   

    def test_mul(self):
        self.assertEqual(Fraction(6,8),Fraction(2,2) * Fraction(3,4))
        self.assertEqual(Fraction(1),Fraction(4,9) * Fraction(9,4))

    def test_sub(self):
        self.assertEqual(Fraction(5,10),Fraction(8,10) - Fraction(3,10))
        self.assertEqual(Fraction(-3,7),Fraction(3,7) - Fraction(6,7))

    def test_gt(self):
        self.assertTrue(Fraction(1,2) > Fraction(1,3))    
        self.assertFalse(Fraction(1,10) > Fraction(1,3))  

    def test_neg(self):
        self.assertEqual(Fraction(1,4), -Fraction(1,-4))
        self.assertEqual(Fraction(-10,20), -Fraction(1,2))

    def test_pow(self):
        self.assertEqual(Fraction(2,3),Fraction(2,3) ** Fraction(2,2))
        self.assertEqual(Fraction(25,36),Fraction(5,6) ** Fraction(2))

    def test_ge(self):
        self.assertTrue(Fraction(2,3) >= Fraction(2,3))
        self.assertFalse(Fraction(5,6) >= Fraction(1))

    def test_truediv(self):
        self.assertEqual(Fraction(1),Fraction(1,2) / Fraction(1,2))
        self.assertEqual(Fraction(4,9),Fraction(2,3) / Fraction(3,2))

    def test_eq(self):
        one = Fraction(1)
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2 
        inf = Fraction(1,0) # infinity value
        negative_inf = Fraction(-1,0) # negative infinity value
        negative_inf2 = Fraction(-12312313131232312,0) #massive number 
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(f == inf) #fracetion != infinity
        self.assertFalse(inf == negative_inf) #infinity != negative infinity 
        self.assertTrue(negative_inf == negative_inf2) #negative infinity == negative infinity 
        self.assertFalse(one == inf ) # 1 != infinity

