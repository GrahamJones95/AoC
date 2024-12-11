def is_neg(a):
    return a < 0

def is_safe(report):
    sign = is_neg(report[1] - report[0])
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        # print("val: {} diff: {} sign: {} check: {}".format(report[i], diff, sign, is_neg(diff) != sign))
        if(diff == 0 or abs(diff) > 3 or is_neg(diff) != sign):
            return False
    return True

with open("day2input.txt") as file:
    reports = [list(map(int, line.rstrip().split(" "))) for line in file]
    safe_ct = 0
    for report in reports:
        safe_ct += 1 if is_safe(report) else 0
    print("Number of safe reports is {}".format(safe_ct))

    safe_ct_2 = 0
    for report in reports:
        for i in range(len(report)+1):
            if(is_safe(report[:i] + report[i+1:])):
                safe_ct_2 += 1
                break
    print("Number of safe with one removed reports is {}".format(safe_ct_2))