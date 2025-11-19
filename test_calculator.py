import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
     def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,2),4)
        self.assertEqual(multiply(-4,4),-16)
        self.assertEqual(multiply(0,1),0)

     def test_divide(self): # 3 assertions
        self.assertEqual(divide(2,2),1)
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(25,5),5)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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
        self.assertAlmostEqual(divide(3,4),5)
        self.assertAlmostEqual(divide(5,12),13)
        self.assertAlmostEqual(divide(8,15),17)



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