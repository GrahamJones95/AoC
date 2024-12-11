import re

with open("day3input.txt") as file:
    total = 0
    for line in file:
        for pair in re.findall("mul\((\d+),(\d+)\)", line):
            # print(pair)
            total += int(pair[0]) * int(pair[1])
    print("The total result of all muls is {}".format(total))

with open("day3input.txt") as file:
    total = 0
    enabled = True
    for line in file:
        for pair in re.findall("mul\((\d+),(\d+)\)|(do)\(\)|(don)'t\(\)", line):
            # print(pair)
            if(pair[2] == "do"):
                enabled = True
            elif(pair[3] == "don"):
                enabled = False
            elif(pair[0] != "" and pair[1] != "" and enabled):
                total += int(pair[0]) * int(pair[1])
    print("The total result of all muls with enabling is {}".format(total))