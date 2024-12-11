search_dirs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def search(i,j,lines):
    found = 0
    for dir in search_dirs:
        inc = 1
        i2 = i
        j2 = j
        for next_char in "MAS":
            i2 += dir[0]
            j2 += dir[1]
            if(i2 < 0 or i2 >= len(lines) or j2 < 0 or j2 >= len(lines[0]) or lines[i2][j2] != next_char):
                inc = 0
        found += inc
    return found

with open("day4input.txt") as file:
    lines = [line.rstrip() for line in file]
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if(lines[i][j] == "X"):
                total += search(i,j,lines)
    print("Total count of XMAS is {}".format(total))


cross_dirs = [((-1,1),(1,-1)),((1,1),(-1,-1))]

def search(i,j,lines):
    for cross_dir in cross_dirs:
        i1 = i+cross_dir[1][0]
        j1 = j+cross_dir[1][1]

        i2 = i+cross_dir[0][0]
        j2 = j+cross_dir[0][1]

        if(i1 < 0 or i1 >= len(lines) or j1 < 0 or j1 >= len(lines[0])):
            return 0
        if(i2 < 0 or i2 >= len(lines) or j2 < 0 or j2 >= len(lines[0])):
            return 0
        if(not (lines[i1][j1] == "S" and lines[i2][j2] == "M" or lines[i1][j1] == "M" and lines[i2][j2] == "S")):
            return 0
    return 1

with open("day4input.txt") as file:
    lines = [line.rstrip() for line in file]
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if(lines[i][j] == "A"):
                total += search(i,j,lines)
    print("Total count of XMAS is {}".format(total))
