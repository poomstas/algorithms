# Tournament Winner
# https://www.algoexpert.io/questions/Tournament%20Winner

# O(N) time | O(k) space, where k is the total number of teams.
def tournamentWinner(competitions, results):
    current_best_team = ""
    current_best_score = 0
    scores = {}
    for competition, result in zip(competitions, results):
        winner = competition[int(not result)]
        if winner not in scores:
            scores[winner] = 0
        scores[winner] += 3

        if scores[winner] > current_best_score:
            current_best_score = scores[winner]
            current_best_team = winner

    return current_best_team


#######################################################################

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
