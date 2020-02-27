import unittest

def first_missing_alphabet(inputString):
	# Find the first missing alphabet character
	fullalphabetstring = "abcdefghijklmnopqrstuvwxyz"

	alphabetregister = {}

	#add letters to dictionary
	for letter in fullalphabetstring:
		alphabetregister[letter] = 0

	lowercaseinputstring = inputString.lower()

	for letter in lowercaseinputstring:
		#check if letter is in alphabetregister as key => abcd... but not @!$...:
		if letter in alphabetregister:
			alphabetregister[letter] = 1

	##check if/which letter is missing
	for k,v in alphabetregister.items():
		if v == 0:
			return k


	return ""

class Fma_tests(unittest.TestCase):
	def test_single_character(self):
		inString = "b"
		expectedMissing = "a"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def emptystring(self):
		inString = ""
		expectedMissing = "a"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def nonalphabeticcharacters(self):
		inString = "@!"
		expectedMissing = "a"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def startingwithlastcharactersofalphabet(self):
		inString = "za"
		expectedMissing = "b"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def recurringcharacters(self):
		inString = "aaaaa"
		expectedMissing = "b"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def providedcomplexstring(self):
		inString = "@aYBed56$=CAg"
		expectedMissing = "f"
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

	def completealphabet(self):
		inString = "abcdefghijklmnopqrstuvwxyz"
		expectedMissing = ""
		foundMissing = first_missing_alphabet(inString)
		self.assertEqual(expectedMissing, foundMissing)

if __name__ == '__main__':
	unittest.main()
