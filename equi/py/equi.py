import unittest

def find_equi_index(inArray, numElements):
	# Find the equilibrium index of input array

	#if inArray is None return -1
	if (len(inArray)<1):
		return -1

	rightsum = sum(inArray)
	leftsum = 0

	for index in range(0,numElements):
		rightsum -= inArray[index]
		if rightsum == leftsum:
			return index

		leftsum += inArray[index]

	return -1

class TestEquiIndex(unittest.TestCase):
	def test_signelNumber(self):
		inArray = [3]
		expectedP = 0
		P = find_equi_index(inArray, len(inArray))
		self.assertEqual(expectedP, P)


if __name__ == '__main__':
	unittest.main()
