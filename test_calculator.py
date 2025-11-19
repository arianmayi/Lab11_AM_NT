#https://github.com/arianmayi/Lab11_AM_NT.git
#Arian Mayi - Partner 1
#Ngoc Tieu - Partner 2

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2


    def test_add(self): # 3 assertions
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add(-5,3), -2)
        self.assertEqual(add(0,10),10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(-4,-6), 2)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,2),4)
        self.assertEqual(mul(-4,4),-16)
        self.assertEqual(mul(0,1),0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2),1)
        self.assertEqual(div(2,4),2)
        self.assertEqual(div(25,5),5)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(8,2), math.log(8,2))
        self.assertAlmostEqual(logarithm(100,10), math.log(100,10))
        self.assertAlmostEqual(logarithm(math.e,2), math.log(math.e,2))

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1,10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4,3),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(8,15),17)



    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-25)

        self.assertAlmostEqual(square_root(4),2)
        self.assertAlmostEqual(square_root(25),5)



    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()