import unittest

def solution(N):
    binary_chain = bin(N).lstrip('0b').strip('0')
    max_gap = 0
    current_gap = 0
    for bit in binary_chain:
        if bit == '0':
            current_gap += 1
            max_gap = max(max_gap, current_gap)
        else:
            current_gap = 0
    return max_gap

class TestSolution(unittest.TestCase):

    def test_9(self):
        self.assertEqual(solution(9), 2)

    def test_529(self):
        self.assertEqual(solution(529), 4)

    def test_20(self):
        self.assertEqual(solution(20), 1)

    def test_15(self):
        self.assertEqual(solution(15), 0)

if __name__ == "__main__":
    unittest.main()
