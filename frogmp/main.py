import unittest

def solution(X, Y, D):
    if Y <= X:
        return 0
    else:
        distance = Y - X
        jumps = distance/D + (1 if distance % D else 0)
        return jumps


class TestSolution(unittest.TestCase):

    def test_same_position_1(self):
        self.assertEqual(solution(1, 1, 0), 0)

    def test_same_position_2(self):
        self.assertEqual(solution(1, 1, 1), 0)

    def test_one_jump_1(self):
        self.assertEqual(solution(2, 4, 2), 1)

    def test_one_jump_2(self):
        self.assertEqual(solution(2, 3, 2), 1)

    def test_two_jumps_1(self):
        self.assertEqual(solution(4, 8, 2), 2)

    def test_two_jumps_2(self):
        self.assertEqual(solution(4, 7, 2), 2)

if __name__ == "__main__":
    unittest.main()
