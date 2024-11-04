import unittest

# Function to be tested
def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Invalid input data type. Expecting float or integer.")
    return (celsius * 9/5) + 32

# Test case class
class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_valid_input(self):
        """Test with valid input data"""
        self.assertEqual(celsius_to_fahrenheit(30), 86.0)
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_edge_case(self):
        """Test with edge case"""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_data_type(self):
        """Test with invalid data type"""
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("30")

if __name__ == '__main__':
    unittest.main()
