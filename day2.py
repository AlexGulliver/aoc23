max_red = 12
max_green = 13
max_blue = 14

inputfile = "input2.txt"

input = open(inputfile, "r")

gamenumber = 0
gametotal = 0

# Splits up lines in the text file
for line in input:
    # Start variable is index of ':'
    start = (line.rfind(':'))
    # Prints each line, removing initial game and : characters as well as space
    game = (line[start+2:])
    # Divides each game into their representative handouts
    handouts = game.split(";")
    validgame = True
    for hand in handouts:
        colours = hand.split(',')
        for y in colours:
            v = y.lstrip()
            if 'red' in v:
                if int(v[:2]) > max_red:
                    validgame = False
            if 'green' in v:
                if int(v[:2]) > max_green:
                    validgame = False
            if 'blue' in v:
                if int(v[:2]) > max_blue:
                    validgame = False
    gamenumber = gamenumber + 1
    if validgame == True:
        gametotal = gametotal + gamenumber
    #print("Game number is", gamenumber)
    
print("Total is" ,gametotal) 