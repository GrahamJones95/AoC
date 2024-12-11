with open("day1input.txt") as file:
    vals = [line.rstrip().split("   ") for line in file]
    l1 = [int(i[0]) for i in vals]
    l2 = [int(i[1]) for i in vals]
    l1.sort()
    l2.sort()
    nums = [abs(l1[i] - l2[i]) for i in range(len(l1))]
    print("Answer to part 1 is: {}".format(sum(nums)))

    l2_ct = {}
    for i in l2:
        if(i in l2_ct):
            l2_ct[i] = l2_ct[i] + 1
        else:
            l2_ct[i] = 1
    similarity = 0    
    for i in l1:
        similarity += i * (l2_ct[i] if i in l2_ct else 0)
    print("Answer to part 2 is {}".format(similarity))