f = open("input.txt", "r")
file_content = f.read()
f.close()

def sumCalib(input):
    # Total gives the total calibration score
    total = 0
    for line in input.splitlines():
        for i in line:
            try:
                int(i)
                break
            except ValueError:
                pass  # Ignore non-integer characters
        for k in reversed(line):
            try:
                int(k)
                break
            except ValueError:
                pass  # Ignore non-integer characters
        number = str(i) + str(k)
        total += int(number)
    return total

print(sumCalib(file_content)) 