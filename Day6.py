from timeit import default_timer as timer

def addtodict(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value

def main():
    data = [int(x) for x in open("resources/day6_input.txt", "r").read().split(",")]
    start = timer()
    newfish = {}
    numfish = len(data)
    for d in data:
        addtodict(newfish, d, 1)
    numdays = 256
    for day in range(numdays):
        if day in newfish:
            addtodict(newfish, day+7, newfish[day])
            addtodict(newfish, day+9, newfish[day])
            numfish += newfish[day]
    end = timer()
    print("Fish after ", numdays, " days: ", numfish)
    print("Elapsed time: ", end - start)

if __name__ == "__main__":
    main()