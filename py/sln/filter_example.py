import unittest

epsilon = 0.001


def fir_filter(inputs):
    coefficients = [0.5, 0.3, 0.2, 0.1]
    filter_len = len(coefficients)
    input_len = len(inputs)
    output_len = input_len+filter_len-1
    output = [0]*output_len

    filter_state = [0]*filter_len
    for sampleIdx in range(0,output_len):
        sample_sum = 0
        filter_state[1:filter_len] = filter_state[0:filter_len-1]
        if sampleIdx < input_len:
            filter_state[0] = inputs[sampleIdx]
        else:
            filter_state[0] = 0

        for cidx, coef in enumerate(coefficients):
            sample_sum += filter_state[cidx]*coef

        output[sampleIdx] = sample_sum
    return output


class TestFIRFilter(unittest.TestCase):

    def test_ZeroInput(self):
        inputs = [0]
        ref_output = [0, 0, 0, 0]
        output = fir_filter(inputs)

        self.assertEqual(ref_output, output)

    def test_ImpulseInput(self):
        inputs = [1.0]
        ref_output = [0.5, 0.3, 0.2, 0.1]
        output = fir_filter(inputs)

        self.assertEqual(ref_output, output)

    def test_OutputLengthWithShortInput(self):
        inputs = [1.0, 1.0]
        ref_output = [0.5, 0.8, 0.5, 0.3, 0.1]
        output = fir_filter(inputs)

        self.AssertListAlmostEqual(ref_output, output, epsilon)

    def test_OutputLengthWithLongInput(self):
        inputs = [1.0, 1.0, 1.0, 1.0, 1.0]
        ref_output = [0.5, 0.8, 1.0, 1.1, 1.1, 0.6, 0.3, 0.1]
        output = fir_filter(inputs)

        self.AssertListAlmostEqual(ref_output, output, epsilon)

    def AssertListAlmostEqual(self, list1, list2, tol):
        self.assertEqual(len(list1), len(list2))
        for a, b in zip(list1, list2):
            self.assertTrue(abs(a-b) < tol)

if __name__ == '__main__':
    unittest.main()