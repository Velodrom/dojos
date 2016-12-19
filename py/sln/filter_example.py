import unittest

epsilon = 0.001

def fir_filter(inputs):
	coefs     = [0.5, 0.3, 0.2, 0.1]
	filterLen = len(coefs)
	inputLen  = len(inputs)
	outputLen = inputLen+filterLen-1
	output    = [0]*outputLen

	filterState = [0]*filterLen
	for sampleIdx in range(0,outputLen):
		sampleSum = 0
		filterState[1:filterLen] = filterState[0:filterLen-1]
		if sampleIdx < inputLen:
			filterState[0] = inputs[sampleIdx]
		else:
			filterState[0] = 0

		for cidx, coef in enumerate(coefs):
			sampleSum += filterState[cidx]*coef

		output[sampleIdx] = sampleSum
	return output

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