import re

inputfile = "inputs/day3.txt"

def is_symbol(character):
    if (character != ".") and (character.isdigit() == False) and ("\n" not in character):
        return True
    else:
        return False

def check_for_symbol(x_start, x_end, y, input):
    # 4 corner cases
    lines = []
    for line in input:
        lines.append(line)
    current_line = lines[y]

    # Top-left corner
    if (x_start == 0) and (y == 0):
        line_below = lines[y+1]
        if(is_symbol(current_line[x_end])):
            return True 

        for character in line_below[:x_end+1]:
            if(is_symbol(character)):
                return True
        
    # Top-right corner
    if (x_end+1 == len(current_line)) and (y == 0):
        line_below = lines[y+1]
        if(is_symbol(current_line[x_start-1])):
                return True
        for character in line_below[x_start-1:x_end]:
            if(is_symbol(character)):
                return True 

    # Bottom-left corner
    if (x_start == 0) and (y+1 == len(lines)):
        line_above = lines[y-1]
        for character in line_above[:x_end+1]:
            if(is_symbol(character)):
                return True 
        if(is_symbol(current_line[x_end])):
                return True 

    # Bottom-right corner
    if (x_end+1 == len(current_line)) and (y+1 == len(lines)):
        line_above = lines[y-1]
        for character in line_above[x_start-1:x_end]:
            if(is_symbol(character)):
                return True 
        print(current_line[x_start-1])
        if(is_symbol(current_line[x_start-1])):
                return True 
        
    # 4 non-corner boundary edge cases 

    # number is on left edge
    if (x_start == 0) and (y != 0) and (y+1 != len(lines)):
        line_above = lines[y-1]
        line_below = lines[y+1]
        for character in line_above[x_start:x_end+1]:
            if(is_symbol(character)):
                return True 
        for character in line_below[x_start:x_end+1]:
            if(is_symbol(character)):
                return True 
        if(is_symbol(current_line[x_end])):
                return True 

    # number is on right edge
    if (x_end+1 == len(current_line)) and (y != 0) and (y+1 != len(lines)):
        line_above = lines[y-1]
        line_below = lines[y+1]
        for character in line_above[x_start-1:x_end]:
            if(is_symbol(character)):
                return True 
        for character in line_below[x_start-1:x_end]:
            if(is_symbol(character)):
                return True 
        if(is_symbol(current_line[x_start-1])):
                return True 

    # number is on top
    if (y == 0) and (x_start != 0) and (x_end+1 != len(current_line)):
        line_below = lines[y+1]
        if(is_symbol(current_line[x_start-1])):
                return True 
        if(is_symbol(current_line[x_end])):
                return True 
        for character in line_below[x_start-1:x_end+1]:
            if(is_symbol(character)):
                return True 

    # number is on bottom
    if (y+1 == len(lines)) and (x_start != 0) and (x_end+1 != len(current_line)):
        line_above = lines[y-1]
        if(is_symbol(current_line[x_start-1])):
                return True 
        if(is_symbol(current_line[x_end])):
                return True 
        for character in line_above[x_start-1:x_end+1]:
            if(is_symbol(character)):
                return True 

    # general case
    else:
        line_above = lines[y-1]
        line_below = lines[y+1]
        if(is_symbol(current_line[x_start-1])):
                return True 
        if(is_symbol(current_line[x_end])):
                return True 
        for character in line_above[x_start-1:x_end+1]:
            if(is_symbol(character)):
                return True 
        for character in line_below[x_start-1:x_end+1]:
            if(is_symbol(character)):
                return True 


with open(inputfile, "r") as input:
    lines = input.readlines()
    y = 0
    total = 0
    for line in lines:
        count = 0
        for number in re.finditer("\d{1,}", line):
            if(check_for_symbol(number.start(), number.end(), y, lines)):
                newnum = int(number.group())
                total = total + newnum
            count += 1
        y = y + 1
        
    print("Part 1 Solution:",total)