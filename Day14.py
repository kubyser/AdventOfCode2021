def addOrInc(a, b, pairs, num):
    if (a, b) in pairs:
        pairs[(a, b)] += num
    else:
        pairs[(a, b)] = num

def main():
    data = open("resources/day14_input.txt").read().splitlines()
    poly = data[0]
    pairs = {}
    pos = 1
    while pos < len(poly):
        a = poly[pos-1]
        b = poly[pos]
        addOrInc(a, b, pairs, 1)
        pos += 1
    rules = {}
    for s in data[2:]:
        s = s.split(" -> ")
        rules[(s[0][0], s[0][1])] = s[1]
#    print(poly)
#    print(rules)
#    print(pairs)
    for step in range(40):
        newpairs = {}
        for (a, b) in pairs:
            if (a, b) in rules:
                c = rules[(a, b)]
                count = pairs[(a, b)]
                addOrInc(a, c, newpairs, count)
                addOrInc(c, b, newpairs, count)
        pairs = newpairs
    letters = {poly[0]: 1}
    mostFreq = [1, poly[0]]
    for (a, b) in pairs:
        if b in letters:
            letters[b] += pairs[(a, b)]
        else:
            letters[b] = pairs[(a, b)]
        if letters[b] > mostFreq[0]:
            mostFreq = [letters[b], b]
    leastFreq = [mostFreq[0], mostFreq[1]]
    for a in letters:
        if letters[a] < leastFreq[0]:
            leastFreq = [letters[a], a]
    print("Final letters:")
    print(letters)
    print(mostFreq, leastFreq)
    print(mostFreq[0] - leastFreq[0])


if __name__ == "__main__":
    main()
