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


def calculateScores(courseInfoRaw, playerInfo):

    courseInfo = {'par': courseInfoRaw.par, 'strokeIndex': courseInfoRaw.strokeIndex}

    gross = calculateGrossScore(courseInfo, playerInfo)
    nett = calculateNetScore(courseInfo, playerInfo)
    stableford = calculateStablefordScore(courseInfo, playerInfo)
    stablefordPoints = calculateStablefordPoints(courseInfo, playerInfo)
    quota = calculateQuotaScore(courseInfo, playerInfo)

    scoringInfo = {'gross': gross, 'net': nett, 'stableford': stableford, 'stablefordPoints': stablefordPoints, 'quota':quota}

    return scoringInfo