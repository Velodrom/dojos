import unittest

def first_missing_alphabet(inputString):
	# Find the first missing alphabet character
	return -1

class Fma_tests(unittest.TestCase):
	def test_single_character(self):
		inString = "b"
		expectedMissing = "a"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)


if __name__ == '__main__':
	unittest.main()
