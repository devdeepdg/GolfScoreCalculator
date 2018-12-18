""""
    This file contains various scoring algorithms used in golf
    reference: http://golfcollege.edu/popular-golf-tournament-formats/
"""


def calculateGrossScore(courseInfo, player1):
    """"
        This method calculates the "gross" score for a player on a given course
        return: score value
    """

    playerScore = player1['score']
    coursePar = courseInfo['par']

    playerScore = sum(playerScore)
    courseParValue = sum(coursePar)

    grossScore = playerScore - courseParValue

    return grossScore


def calculateNetScore(courseInfo, player1):
    """"
        This method calculates the "net" score for a player on a given course
        return: score value
    """

    playerScore = player1['score']
    coursePar = courseInfo['par']
    playerHandicap = player1['handicap']

    playerScore = sum(playerScore)
    courseParValue = sum(coursePar)

    netScore = playerScore - courseParValue - playerHandicap

    return netScore


def calculateStablefordScore(courseInfo, player):
    """"
        This method calculates the "stableford" score for a player on a given course
        return: score value
    """

    playerScore = player['score']
    coursePar = courseInfo['par']
    playerHandicap = player['handicap']
    courseStroke = courseInfo['strokeIndex']

    points = 0

    for i in range(18):
        if courseStroke[i] <= playerHandicap:
            playerScore[i] -= 1

        diff = playerScore[i] - coursePar[i]
        if diff >= 2:
            points += 0
        elif diff == 1:
            points += 1
        elif diff == 0:
            points += 2
        elif diff == -1:
            points += 3
        elif diff == -2:
            points += 4
        elif diff == -3:
            points += 5
        elif diff == -4:
            points += 6

    return points


def calculateStablefordPoints(courseInfo, player):
    """"
        This method calculates the "stableford" points for a player on a given course
        return: points value
    """

    playerScore = player['score']
    coursePar = courseInfo['par']
    playerHandicap = player['handicap']
    courseStroke = courseInfo['strokeIndex']

    points = 0

    for i in range(18):
        if courseStroke[i] <= playerHandicap:
            playerScore[i] -= 1
        diff = playerScore[i] - coursePar[i]
        if diff >= 2:
            points -= 3
        elif diff == 1:
            points -= 1
        elif diff == 0:
            points += 0
        elif diff == -1:
            points += 2
        elif diff == -2:
            points += 5
        elif diff == -3:
            points += 8

    return points


def calculateBetterBallGrossScore(courseInfo, player1, player2):
    """"
        This method calculates the "gross better ball" score between 2 players on a given course
        return: score value
    """

    player1Score = player1['score']
    player2Score = player2['score']
    coursePar = courseInfo['par']

    betterBallScore = []

    for i in range(18):
        if player1Score[i] < player2Score[i]:
            betterBallScore.append(player1Score[i])
        elif player2Score[i] > player1Score[i]:
            betterBallScore.append(player2Score[i])
        else:
            betterBallScore.append(player1Score[i])

    courseParValue = sum(coursePar)
    playerScore = sum(betterBallScore)

    grossScore = playerScore - courseParValue

    return grossScore


def calculateBetterBallNetScore(courseInfo, player1, player2):
    """"
        This method calculates the "net better ball" score between 2 player on a given course
        return: score value
    """

    player1Score = player1['score']
    player2Score = player2['score']
    coursePar = courseInfo['par']
    player1Handicap = player1['handicap']
    player2Handicap = player2['handicap']
    courseStroke = courseInfo['strokeIndex']

    betterBallScore = []

    for i in range(18):
        if courseStroke[i] <= player1Handicap:
            player1Score[i] -= 1
        if courseStroke[i] <= player2Handicap:
            player2Score[i] -= 1

        if player1Score[i] < player2Score[i]:
            betterBallScore.append(player1Score[i])
        elif player2Score[i] > player1Score[i]:
            betterBallScore.append(player2Score[i])
        else:
            betterBallScore.append(player1Score[i])

    courseParValue = sum(coursePar)
    playerScore = sum(betterBallScore)

    netScore = playerScore - courseParValue

    return netScore


def calculateQuotaScore(courseInfo, player):
    """"
        This method calculates the "quota" score for a player on a given course
        return: score value
    """

    playerScore = player['score']
    coursePar = courseInfo['par']
    playerHandicap = player['handicap']
    courseStroke = courseInfo['strokeIndex']

    points = 0

    for i in range(18):
        if courseStroke[i] <= playerHandicap:
            playerScore[i] -= 1

        diff = playerScore[i] - coursePar[i]

        if diff == 1:
            points += 1
        elif diff == 0:
            points += 2
        elif diff == -1:
            points += 4
        elif diff == -2:
            points += 8

    points = points + playerHandicap

    return points
