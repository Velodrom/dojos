import unittest
def find_equi_index(inArray, numElements):
    upper_index_sum= 0
    for x in range(numElements):
        upper_index_sum = upper_index_sum + inArray[x]
    lower_index_sum =0
    for i in range(numElements):
        lower_index_sum = lower_index_sum + inArray[i]
        if lower_index_sum == upper_index_sum:
            return i
        upper_index_sum = upper_index_sum - inArray[i]
    return -1

class TestEquiIndex(unittest.TestCase):
    def test_signelNumber(self):
        inArray = [2,-3,4,-2,1]
        expectedP = 0
        P = find_equi_index(inArray, len(inArray))
        self.assertEqual(expectedP, P)


if __name__ == '__main__':
    unittest.main()