import unittest

def solution(S, P, Q):
    impacts = {
               "A": 1,
               "C": 2,
               "G": 3,
               "T": 4
            }
    result = [] 
    for i,j in zip(P,Q):
        result.append(min(map(lambda x: impacts[x], S[i:j+1])))
    return result

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]), [2, 4, 1])

if __name__ == "__main__":
    unittest.main()
