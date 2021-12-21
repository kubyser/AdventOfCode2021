diceNextNum = 1
diceNumRolled = 0


def rollDetermenisticDice(num):
    global diceNextNum
    global diceNumRolled
    score = 0
    for i in range(num):
        score += diceNextNum
        diceNextNum += 1
        if diceNextNum > 100:
            diceNextNum -= 100
        diceNumRolled += 1
    return score, diceNumRolled


def runPart1():
    pos = [3, 7]
    score = [0, 0]
    player = 0
    diceRolled = 0
    while score[0] < 1000 and score[1] < 1000:
        diceScore, diceRolled = rollDetermenisticDice(3)
        pos[player] += diceScore
        print("==== Player ", player)
        print("Dice score: ", diceScore)
        if pos[player] % 10 == 0:
            pos[player] = 10
        else:
            pos[player] = pos[player] % 10
        print("Pos: ", pos[player])
        score[player] += pos[player]
        print("Score: ", score[player])
        player = 0 if player == 1 else 1
    res = score[player] * diceRolled
    print(res)


def runPart2():
    diceRes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    #scores = [{(0, 4): 1}, {(0, 8): 1}]
    scores = [{(0, 3): 1}, {(0, 7): 1}]
    winningUniverses = [0, 0]
    player = 0
    while len(scores[0]) > 0 or len(scores[1]) > 0:
        otherPlayer = 0 if player == 1 else 1
        if len(scores[player]) > 0:
            newScores = {}
            for a in diceRes:
                for (s, p) in scores[player]:
                    newPos = p + a
                    if newPos > 10:
                        newPos = newPos % 10
                    newScore = s + newPos
                    toAddUniverses = scores[player][(s, p)] * diceRes[a]
                    if (newScore, newPos) in newScores:
                        newScores[(newScore, newPos)] += toAddUniverses
                    else:
                        newScores[(newScore, newPos)] = toAddUniverses
            numWins = 0
            scores[player] = {}
            for (s, p) in newScores:
                if s >= 21:
                    numWins += newScores[(s, p)]
                else:
                    scores[player][(s, p)] = newScores[(s, p)]
            numOtherUniverses = 0
            for (os, op) in scores[otherPlayer]:
                numOtherUniverses += scores[otherPlayer][(os, op)]
            winningUniverses[player] += numWins * numOtherUniverses
        player = otherPlayer
    print(winningUniverses)
    print("Part 2: number of universes in which luckiest player wins: ", max(winningUniverses))


def main():
    runPart2()


if __name__ == "__main__":
    main()



