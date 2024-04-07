max_red = 12
max_green = 13
max_blue = 14

inputfile = "inputs/day2.txt"

input = open(inputfile, "r")

gamenumber = 0
gametotal = 0
powertotal = 0
# Splits up lines in the text file
for line in input:
    # Start variable is index of ':'
    start = (line.rfind(':'))
    # Prints each line, removing initial game and : characters as well as space
    game = (line[start+2:])
    # Divides each game into their representative handouts
    handouts = game.split(";")
    validgame = True
    reds = []
    blues = []
    greens = []
    for hand in handouts:
        colours = hand.split(',')
        for y in colours:
            v = y.lstrip()
            if 'red' in v:
                reds.append(int(v[:2]))
                if int(v[:2]) > max_red:
                    validgame = False
            if 'green' in v:
                greens.append(int(v[:2]))
                if int(v[:2]) > max_green:
                    validgame = False
            if 'blue' in v:
                blues.append(int(v[:2]))
                if int(v[:2]) > max_blue:
                    validgame = False
    reds.sort()
    greens.sort()
    blues.sort()
    print(reds)
    print(greens)
    print(blues)
    power = reds[-1] * greens[-1] * blues[-1]
    print(power)
    powertotal += power
    print("POWERTOTAL", powertotal)
    print("end of game")
    gamenumber = gamenumber + 1
    if validgame == True:
        gametotal = gametotal + gamenumber
    #print("Game number is", gamenumber)

# Part 1 solution
print("Total is" ,gametotal) 

#Part 2 solution
print("Power total = ", powertotal)