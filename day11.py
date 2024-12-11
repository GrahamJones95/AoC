input = [1950139, 0, 3, 837, 6116, 18472, 228700, 45]
input2 = [125, 17]

def transform(val):
        if(val == 0):
            return [1]
        elif(len(str(val)) % 2 == 0):
            return [int(str(val)[:len(str(val))//2]), int(str(val)[len(str(val))//2:])]
        else:
             return [val * 2024]

def blink(input):
    new_list = []
    for i in input:
        new_list.extend(transform(i))
    return new_list


# total = 0
# for i in input:
#     new_input = [i]
#     for j in range(25):
#         new_input = blink(new_input)
#     total += len(new_input)
# print(total)

#DFS
def blink_rec(input, depth):
    if(depth == 0):
          return len(input)
    total = 0
    for i in input:
        for j in blink([i]):
            total += blink_rec([j], depth-1)
    return total

print(blink_rec(input, 75))
