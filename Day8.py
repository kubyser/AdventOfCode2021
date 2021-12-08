def hasall(s1, s2):
    for s in s2:
        if s not in s1:
            return False
    return True

def main():
    data = open("resources/day8_input.txt", "r").read().splitlines()
    sym = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
    sum = 0

    for dl in data:
        d = dl.split(" | ")
        inp = [sorted(x) for x in d[0].split()]
        ans = {}
        r1 = next(filter(lambda x: len(x) == 2, inp))
        r7 = next(filter(lambda x: len(x) == 3, inp))
        r4 = next(filter(lambda x: len(x) == 4, inp))
        r9 = next(filter(lambda a: hasall(a, r1) and hasall(a, r4), filter(lambda x: len(x) == 6, inp)))
        aa = next(filter(lambda x: x not in r1, r7))
        ag = next(filter(lambda x: x not in r1 and x not in r4 and x not in r7, r9))
        r3 = next(filter(lambda a: hasall(a, r1) and aa in a and ag in a, filter(lambda x: len(x) == 5, inp)))
        ad = next(filter(lambda x: x not in r1 and x not in [aa, ag], r3))
        ab = next(filter(lambda x: x not in r1 and x != ad, r4))
        r0 = next(filter(lambda a: ad not in a, filter(lambda x: len(x) == 6, inp)))
        ae = next(filter(lambda x: x not in r7 and x not in [ab, ag], r0))
        r2 = next(filter(lambda a: ae in a, filter(lambda x: len(x) == 5, inp)))
        ac = next(filter(lambda x: x not in [aa, ad, ae, ag], r2))
        af = next(filter(lambda x: x not in [ac], r1))
        ans[aa] = 'a'
        ans[ab] = 'b'
        ans[ac] = 'c'
        ans[ad] = 'd'
        ans[ae] = 'e'
        ans[af] = 'f'
        ans[ag] = 'g'

        res = d[1].split()
        num = 0
        for r in res:
            str = ""
            for c in r:
                str += ans[c]
            str = "".join(sorted(str))
            num = num*10 + sym[str]
        sum += num
        #print(res, num)
    print("Result: ", sum)

if __name__ == "__main__":
    main()