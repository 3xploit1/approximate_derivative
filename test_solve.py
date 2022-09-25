import unittest 
from main import Solve

class TestSolve(unittest.TestCase):
    ##
    def setUp(self):
        self.sol = Solve() 
    
    def test_1(self):
        self.assertEqual(self.sol.solve(5, 2), 30.0)
    
    def test_2(self):
        self.assertEqual(self.sol.solve(3, 2), 18.0)
    
    def test_3(self):
        self.assertEqual(self.sol.solve(-0.3, 2), -1.8)
    
    def test_4(self):
        self.assertEqual(self.sol.solve(1, 2), 6.0)
    
    def test_5(self):
        self.assertEqual(self.sol.solve(5.1, 2), 30.6)
    
    def test_6(self):
        self.assertEqual(self.sol.solve(0.1, 2), 0.6)
    
    def test_7(self):
        self.assertEqual(self.sol.solve(0.4, 2), 2.4)
    
    def test_8(self):
        self.assertEqual(self.sol.solve(2, 2), 12.0) 
    
    def test_9(self):
        self.assertEqual(self.sol.solve(10, 2), 60.0) 
    
    def test_10(self):
        self.assertEqual(self.sol.solve(33, 2), 198.0)
    
    def test_11(self):
        self.assertEqual(self.sol.solve(99, 2), 594)
    
    def test_12(self):
        self.assertEqual(self.sol.solve(-1, 2), -6)
    
    def test_13(self):
        self.assertEqual(self.sol.solve(0.1111, 2), 0.6666)
    
    def test_14(self):
        self.assertEqual(self.sol.solve(-0.04, 2), -0.24)
    
    def test_15(self):
        self.assertEqual(self.sol.solve(0.999999, 2), 6.0) 
    
if __name__ == "__main__": 
    unittest.main()
    
    
    