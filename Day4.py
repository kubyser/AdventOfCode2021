from Bingo import Bingo

def main():
    bingo = Bingo(open("resources/day4_input.txt", "r").read().splitlines())
    res = bingo.playBingo(True)
    print("Result: ", res)

if __name__ == "__main__":
    main()