import unittest

def solution(A, K):
    if len(A) < 1:
        return A
    for i in range(K):
        element = A.pop()
        A.insert(0, element)
    return A

class TestSolution(unittest.TestCase):

    def test_empty_1(self):
        self.assertEqual(solution([], 1), [])

    def test_empty_2(self):
        self.assertEqual(solution([], 2), [])

    def test_one_element_1(self):
        self.assertEqual(solution([5], 1), [5])

    def test_one_element_2(self):
        self.assertEqual(solution([5], 2), [5])

    def test_1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 1), [6, 3, 8, 9, 7])

    def test_2(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 2), [7, 6, 3, 8, 9])

    def test_3(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_4(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 4), [8, 9, 7, 6, 3])

    def test_5(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 5), [3, 8, 9, 7, 6])

if __name__ == "__main__":
    unittest.main()
