def solve(num_keyboards, num_notes, keyboards, melody):
    bool_keyboards = [{i:False for i in set(melody)} for j in range(0, num_keyboards)]
    # print(np.array(bool_keyboards).shape)
    for i in range(0, num_keyboards):
        for j in range(1, len(keyboards[i])):
            bool_keyboards[i][keyboards[i][j]] = True
    active_keyboards = list(range(0, num_keyboards))
    counter = 0
    for i in range(0, num_notes):
        # deleted = set()
        active_now = []
        for j in active_keyboards:
            if bool_keyboards[j][melody[i]] == True:
                active_now.append(j)
        active_keyboards = active_now
        if len(active_keyboards) == 0:
            counter = counter + 1
            active_keyboards = []
            for p in range(0, num_keyboards):
                if bool_keyboards[p][melody[i]]:
                    active_keyboards.append(p)
  	          
    return counter

# def worstcase():
#     from random import randint
#     tune = [randint(1, 999) for i in range (0, 1000)]
#     keyboards = []
#     for i in range(0, 1000):
#         size = randint(50, 1000)
#         kb = [size + 1, i]
#         for count in range(size - 1):
#             kb.append(randint(1, 999))
#         keyboards.append(kb)
#     solve(1000, 1000, keyboards,  tune)
# worstcase()

import sys
def read_input():
    i = input()
    r = i.split(" ")
    m = int(r[0])
    n = int(r[1])

    inc = int(r[0])
    keyboards = []
    while inc > 0:
        keyboards.append(list(map(int, input().split(" "))))
        inc = inc - 1
    tune = list(map(int, input().split(" ")))   # return sys.stdin.readlines()
    return [m, n, keyboards, tune]

args = read_input()
print(solve(*args))