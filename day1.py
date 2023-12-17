f = open("input.txt", "r")
inputFile = f.read()
f.close()

def sumCalib(input):
    total = 0
    stringNumbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    for line in input.splitlines():
        print(line)
        fn = False
        i = 0

        while not fn and i < len(line):
            if line[i].isdigit() or line[i+1].isdigit():
                firstNum = int(line[i]) if line[i].isdigit() else int(line[i+1])
                fn = True
            else:
                searchFromFront = line[i:i + 5]
                if any(digitWord in searchFromFront for digitWord in stringNumbers):
                    for digitWord in stringNumbers:
                        if digitWord in searchFromFront:
                            firstNum = stringNumbers.index(digitWord) + 1
                            if 1 <= firstNum <= 9:
                                fn = True
                                break  # exit the loop when a match is found
                else:
                    pass  # do nothing

            i += 1
        print("first num", firstNum)

        ln = False
        k = 0
        backwardsText = line[::-1]
        while not ln and k < len(line):
            if backwardsText[k].isdigit():
                lastNum = backwardsText[k]
            if backwardsText[k].isdigit() or backwardsText[k+1].isdigit():
                lastNum = int(backwardsText[k]) if backwardsText[k].isdigit() else int(backwardsText[k+1])
                ln = True
                break
            else:
                reversedSearchSpace = backwardsText[k:k + 5]
                searchFromBack = reversedSearchSpace[::-1]
                if reversedSearchSpace[0].isdigit():
                    lastNum = searchFromBack[0]
                    ln = True
                    break
                elif any(digitWord in searchFromBack for digitWord in stringNumbers):
                    for digitWord in stringNumbers:
                        if digitWord in searchFromBack:
                            lastNum = stringNumbers.index(digitWord) + 1
                            if 1 <= lastNum <= 9:
                                ln = True
                                break

                pass

            k += 1
        print("last num", lastNum)
        number = str(firstNum) + str(lastNum)
        print("number", number)
        total += int(number)
    print("total", total)
    return(total)

sumCalib(inputFile)      