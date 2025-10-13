import unittest
import sys
import os

# Add parent directory to path to import discriminant module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from discriminant import calculate_discriminant, solve_quadratic


class TestDiscriminant(unittest.TestCase):
    """Test cases for discriminant calculation"""
    
    # Positive tests - discriminant >= 0
    
    def test_positive_discriminant(self):
        """Test case with positive discriminant (D > 0)"""
        result = calculate_discriminant(1, -3, 2)
        self.assertEqual(result, 1)
    
    def test_zero_discriminant(self):
        """Test case with zero discriminant (D = 0)"""
        result = calculate_discriminant(1, -2, 1)
        self.assertEqual(result, 0)
    
    def test_negative_discriminant(self):
        """Test case with negative discriminant (D < 0)"""
        result = calculate_discriminant(1, 1, 1)
        self.assertEqual(result, -3)
    
    # Test solve_quadratic function
    
    def test_solve_two_roots(self):
        """Test solving quadratic equation with two roots"""
        roots = solve_quadratic(1, -3, 2)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 1.0)
    
    def test_solve_one_root(self):
        """Test solving quadratic equation with one root"""
        roots = solve_quadratic(1, -2, 1)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1.0)
    
    def test_solve_no_real_roots(self):
        """Test solving quadratic equation with no real roots"""
        roots = solve_quadratic(1, 1, 1)
        self.assertEqual(len(roots), 0)
    
    # Edge cases
    
    def test_invalid_coefficient_a(self):
        """Test with invalid coefficient a = 0"""
        with self.assertRaises(ValueError):
            calculate_discriminant(0, 1, 1)
    
    def test_float_coefficients(self):
        """Test with float coefficients"""
        result = calculate_discriminant(1.5, 2.5, 1.0)
        self.assertAlmostEqual(result, 0.25)
    
    def test_negative_coefficients(self):
        """Test with negative coefficients"""
        result = calculate_discriminant(-1, -2, -3)
        self.assertEqual(result, -8)


if __name__ == '__main__':
    unittest.main()