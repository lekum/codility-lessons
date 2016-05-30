import unittest

def solution(A):
    if len(A) == 1:
        return A[0]
    seen = set()
    candidates = set(A)
    for i in A:
        if i in seen:
            candidates.discard(i)
        else:
            seen.add(i)
    return candidates.pop()

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

    def test_2(self):
        self.assertEqual(solution([6, 9, 9, 7, 6]), 7)

    def test_3(self):
        self.assertEqual(solution([6, 9, 6]), 9)

    def test_6(self):
        self.assertEqual(solution([6]), 6)

if __name__ == "__main__":
    unittest.main()
