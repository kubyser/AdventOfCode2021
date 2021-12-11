def main():
    data = open("resources/day10_input.txt").read().splitlines()
    match = {'(': ')', '[': ']', '<': '>', '{': '}'}
    corruptScoreMap = {')': 3, ']': 57, '}': 1197, '>': 25137}
    incompleteScoreMap = {')': 1, ']': 2, '}': 3, '>': 4}
    corruptedScore = 0
    incompleteScores = []
    for s in data:
        stack = []
        corrupted = False
        for c in s:
            if c in match:
                stack.append(c)
            else:
                exp = match[stack.pop()]
                if c != exp:
                    corruptedScore += corruptScoreMap[c]
                    corrupted = True
                    break
        if not corrupted and len(stack) > 0:
            incompleteScore = 0
            while len(stack) > 0:
                incompleteScore *= 5
                incompleteScore += incompleteScoreMap[match[stack.pop()]]
            incompleteScores.append(incompleteScore)
            #print(incompleteScore)

    incompleteScores.sort()
    middleIncompleteScore = incompleteScores[round(len(incompleteScores) / 2)]
    print("Corrupted score: ", corruptedScore)
    print("Incomplete score: ", middleIncompleteScore)

if __name__ == "__main__":
    main()


