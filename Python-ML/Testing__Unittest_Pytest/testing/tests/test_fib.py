'''
unit tests - checks a small component in your application

integration tests - testing multiple components and if they can
operate with each other 
    problem: when test fails, hard to find root problem
'''
import unittest
from fibonnacci.fib import fibonacci_calculator

class Test_Fib(unittest.TestCase):
    
    def test(self):
        result = fibonacci_calculator(6)
        self.assertEqual(result, 8)
    #integration test
    assert fibonacci_calculator(6) == 8, "number should be 8"
   
    # To run in bash: python -m unittest discover tests
    if __name__ == "__main__":
        unittest.main()
        print("Passed")