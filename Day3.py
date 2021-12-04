f = open("day3_input.txt", "r")
lines = f.read().splitlines()
f.close()

gamma = [1 if sum(int(a[x]) for a in lines)/len(lines) >= 0.5 else 0 for x in range(len(lines[0]))]
gammaDec = int("".join(str(x) for x in gamma), 2)
epsilon = [0 if sum(int(a[x]) for a in lines)/len(lines) >= 0.5 else 1 for x in range(len(lines[0]))]
epsilonDec = int("".join(str(x) for x in epsilon), 2)
power = gammaDec * epsilonDec

print(lines)
print("Gamma=", gamma, " = ", gammaDec)
print("Epsilon=", epsilon, " = ", epsilonDec)
print("Power=", power)

print("======= Part2 =======")

oxygen = lines
pos = 0
while len(oxygen) > 1:
    keep = '1' if sum(int(a[pos]) for a in oxygen) / len(oxygen) >= 0.5 else '0'
    oxygen = list(filter(lambda x: x[pos] == keep, oxygen))
    pos = pos+1

oxygenDec = int(oxygen[0], 2)
print(oxygenDec)

co2 = lines
pos = 0
while len(co2) > 1:
    keep = '0' if sum(int(a[pos]) for a in co2) / len(co2) >= 0.5 else '1'
    co2 = list(filter(lambda x: x[pos] == keep, co2))
    pos = pos+1

co2Dec = int(co2[0], 2)
print(co2Dec)

lifeSupport = oxygenDec * co2Dec
print("Answer=", lifeSupport)
