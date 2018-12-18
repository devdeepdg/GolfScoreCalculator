""""
    This file contains the unit test cases for all methods in scores.py
"""
from unittest import TestCase

from scores import calculateGrossScore, calculateNetScore, calculateStablefordScore, calculateStablefordPoints, calculateBetterBallGrossScore, calculateBetterBallNetScore, calculateQuotaScore


class testScores(TestCase):
    """"
        Unit test case class
    """

    courseInfo = {'name': "Tollygunge Club",
                  'location': ['kolkata', 'india'],
                  'par': [4, 3, 4, 4, 4, 3, 5, 3, 4, 5, 3, 4, 5, 4, 4, 4, 4, 3],
                  'strokeIndex': [7, 17, 3, 11, 1, 13, 9, 15, 5, 14, 16, 10, 4, 12, 6, 2, 8, 18]}

    player1 = {'name': "DDG",
               'handicap': 10,
               'score': [4, 3, 4, 4, 4, 3, 5, 3, 4, 5, 3, 4, 5, 4, 4, 4, 4, 3]}

    player2 = {'name': "Nak",
               'handicap': 18,
               'score': [5, 4, 5, 5, 5, 4, 6, 4, 5, 6, 4, 5, 6, 5, 5, 5, 5, 4]}

    def testGrossScore(self):
        """"
            Unit tests for calculateGrossScore() using data initialized above
        """

        score = calculateGrossScore(self.courseInfo, self.player1)
        self.assertEqual(score, 0)

        score = calculateGrossScore(self.courseInfo, self.player2)
        self.assertEqual(score, 18)

    def testNetScore(self):
        """"
            Unit tests for calculateNetScore() using data initialized above
        """

        score = calculateNetScore(self.courseInfo, self.player1)
        self.assertEqual(score, -10)

        score = calculateNetScore(self.courseInfo, self.player2)
        self.assertEqual(score, 0)

    def testStablefordScore(self):
        """"
            Unit tests for calculateStablefordScore() using data initialized above
        """

        score = calculateStablefordScore(self.courseInfo, self.player1)
        self.assertEqual(score, 46)

        score = calculateStablefordScore(self.courseInfo, self.player2)
        self.assertEqual(score, 36)

    def testStablefordPoints(self):
        """"
            Unit tests for calculateStablefordPoints() using data initialized above
        """

        score = calculateStablefordPoints(self.courseInfo, self.player1)
        self.assertEqual(score, 20)

        score = calculateStablefordPoints(self.courseInfo, self.player2)
        self.assertEqual(score, 0)

    def testBetterBallGrossScore(self):
        """"
            Unit tests for calculateBetterBallGrossScore() using data initialized above
        """

        score = calculateBetterBallGrossScore(self.courseInfo, self.player1, self.player2)
        self.assertEqual(score, 0)

    def testBetterBallNetScore(self):
        """"
            Unit tests for calculateBetterBallNetScore() using data initialized above
        """

        score = calculateBetterBallNetScore(self.courseInfo, self.player1, self.player2)
        self.assertEqual(score, -10)

    def testQuotaScore(self):
        """"
            Unit tests for calculateQuotaScore() using data initialized above
        """

        score = calculateQuotaScore(self.courseInfo, self.player1)
        self.assertEqual(score, 66)

        score = calculateQuotaScore(self.courseInfo, self.player2)
        self.assertEqual(score, 54)


