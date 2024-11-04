import unittest

# Function to be tested
def transform_data(data):
	return [item.upper() for item in data]

class TestDataTransformation(unittest.TestCase):

	def test_transformed_data_correct(self):
		input_data = ['hello', 'python', 'coders']
		expected_output = ['HELLO', 'PYTHON', 'CODERS']
		result = transform_data(input_data)
		self.assertEqual(result, expected_output)

if __name__ == '__main__':
	unittest.main()
