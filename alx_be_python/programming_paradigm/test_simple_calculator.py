import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Test negative results
        self.assertEqual(self.calc.subtract(5, 8), -3)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-2, -5), 3)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        # Test decimal results
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        # Test division by zero - should return None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()