TYPE_SUM = 0
TYPE_PRODUCT = 1
TYPE_MINIMUM = 2
TYPE_MAXIMUM = 3
TYPE_LITERAL = 4
TYPE_GREATERTHAN = 5
TYPE_LESSTHAN = 6
TYPE_EQUALTO = 7

LENGTH_TYPE_BITS = 0
LENGTH_TYPE_PACKETS = 1

hexToBin = {'0': "0000",
            '1': "0001",
            '2': "0010",
            '3': "0011",
            '4': "0100",
            '5': "0101",
            '6': "0110",
            '7': "0111",
            '8': "1000",
            '9': "1001",
            'A': "1010",
            'B': "1011",
            'C': "1100",
            'D': "1101",
            'E': "1110",
            'F': "1111"}

def parsePacket(s, startpos, optype, ltype, num):
    print(s)
    doneParsing = False
    packpos = startpos
    packetsProcessed = 0
    versionsum = 0
    finalValue = 0 if optype in {TYPE_SUM} else 1 if optype in {TYPE_PRODUCT} else None
    while not doneParsing:
        packetsProcessed += 1
        version = int(s[packpos: packpos+3], 2)
        versionsum += version
        type = int(s[packpos+3: packpos+6], 2)
        print("Version: ", version)
        print("Type: ", type)
        val = None
        if type == TYPE_LITERAL:
            stop = False
            pos = packpos+6
            binval = ""
            while not stop:
                group = s[pos: pos+5]
                stop = group[0] == '0'
                binval += group[1:]
                pos += 5
            val = int(binval, 2)
            print("Value: ", val)
            packpos = pos
        else:
            lt = int(s[packpos+6])
            lval = int(s[packpos+7: packpos+7+15], 2) if lt == LENGTH_TYPE_BITS else int(s[packpos+7: packpos+7+11], 2)
            (packpos, val, vsum) = parsePacket(s, packpos+7+15 if lt == LENGTH_TYPE_BITS else packpos+7+11, type, lt, lval)
            versionsum += vsum
        if optype == TYPE_SUM:
            finalValue += val
        elif optype == TYPE_PRODUCT:
            finalValue *= val
        elif optype == TYPE_MINIMUM:
            if finalValue == None or finalValue > val:
                finalValue = val
        elif optype == TYPE_MAXIMUM:
            if finalValue == None or finalValue < val:
                finalValue = val
        elif optype == TYPE_GREATERTHAN:
            if finalValue == None:
                finalValue = val
            else:
                finalValue = 1 if finalValue > val else 0
        elif optype == TYPE_LESSTHAN:
            if finalValue == None:
                finalValue = val
            else:
                finalValue = 1 if finalValue < val else 0
        elif optype == TYPE_EQUALTO:
            if finalValue == None:
                finalValue = val
            else:
                finalValue = 1 if finalValue == val else 0
        else:
            finalValue = None
        doneParsing = packetsProcessed == num if ltype == LENGTH_TYPE_PACKETS else packpos == startpos + num
    return (packpos, finalValue, versionsum)


def main():
    #data = "D2FE28"
    #data = "38006F45291200"
    #data = "EE00D40C823060"
    #data = "8A004A801A8002F478"
    #data = "620080001611562C8802118E34"
    #data = "C0015000016115A2E0802F182340"
    #data = "A0016C880162017C3686B18A3D4780"
    #data = "C200B40A82"
    #data = "04005AC33890"
    #data = "880086C3E88112"
    #data = "CE00C43D881120"
    #data = "D8005AC2A8F0"
    #data = "F600BC2D8F"
    #data = "9C005AC2F8F0"
    #data = "9C0141080250320F1802104A08"
    data = open("resources/day16_input.txt").read().splitlines()[0]
    s = ""
    for d in data:
        s += hexToBin[d]
    (val, vsum) = parsePacket(s, 0, TYPE_SUM, LENGTH_TYPE_PACKETS, 1)[1:]
    print("Sum of version: ", vsum)
    print("Final value: ", val)

if __name__ == "__main__":
    main()
