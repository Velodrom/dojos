import unittest

epsilon = 0.001

# Implement this filter function
def fir_filter(inputs):
	coefs = [0.5, 0.3, 0.2, 0.1]
	return None

class TestFIRFilter(unittest.TestCase):

	def test_zeroInput(self):
		inputs    = [0]
		refOutput = [0, 0, 0, 0]
		output    = fir_filter(inputs)

		self.assertEqual(refOutput, output)

	def test_impulseInput(self):
		inputs    = [1.0]
		refOutput = [0.5, 0.3, 0.2, 0.1]
		output    = fir_filter(inputs)

		self.assertEqual(refOutput, output)

	def test_outputLength(self):
		inputs    = [1.0, 1.0]
		refOutput = [0.5, 0.8, 0.5, 0.3, 0.1]
		output    = fir_filter(inputs)

		self.assertListAlmostEqual(refOutput, output, epsilon)

	def assertListAlmostEqual(self, list1, list2, tol):
		self.assertEqual(len(list1), len(list2))
		for a, b in zip(list1, list2):
			self.assertTrue(abs(a-b) < tol)

if __name__ == '__main__':
	unittest.main()