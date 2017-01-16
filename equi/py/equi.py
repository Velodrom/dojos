import unittest

def find_equi_index(inArray, numElements):
	# Find the equilibrium index of input array
	return -1

class TestEquiIndex(unittest.TestCase):
	def test_signelNumber(self):
		inArray = [3]
		expectedP = 0
		P = find_equi_index(inArray, len(inArray))
		self.assertEqual(expectedP, P)


if __name__ == '__main__':
	unittest.main()