import unittest
import string 

def first_missing_alphabet(inputString):
  # Find the first missing alphabet character
  
  #Extract alphabet from string
  alphaString = ""
  for char in inputString:
    if char.isalpha():
      alphaString += char
  
    # Convert string to lower case and sorted
  alphaSorted = sorted(alphaString.lower())
    
    #Remove duplicate value 
  alphaUnique = list(dict.fromkeys(alphaSorted))
    
    # Create empty list for storing all missing
    # characters in alphabetical order
  letter = []
  for letters in string.ascii_lowercase:
    if letters not in alphaUnique:
      letter.append(letters)

  print ("List of missing characters in", inputString)
  print (letter)
  return (letter[0])

class Fma_tests(unittest.TestCase):
  def test_single_character(self):
    inString = "@aYBed56$=CAg"
    expectedMissing = "f"
    foundMissing = first_missing_alphabet(inString)
    self.assertEqual(expectedMissing, foundMissing)
    if expectedMissing == foundMissing:
      print ("The first missing alphabet is", foundMissing)
  
if __name__ == '__main__':
  unittest.main()
