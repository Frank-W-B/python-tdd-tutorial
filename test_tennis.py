from tennis import Set, Scores
from unittest import TestCase

class TestSetWinning(TestCase):
    def test_score_grows(self):
        set = Set()
        self.assertEqual("0", set.firstScore())
        set.firstScores()
        self.assertEqual("15", set.firstScore())

class TestScoreNames(TestCase):
    def test_score_names(self):
        scores = Scores()
        self.assertEqual("0", scores.scoreName(0))
        self.assertEqual("15", scores.scoreName(1))
        self.assertEqual("30", scores.scoreName(2))
        self.assertEqual("40", scores.scoreName(3))
        self.assertEqual("A", scores.scoreName(4))