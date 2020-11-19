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

def solve(num_keyboards, num_notes, keyboards, tune):
    bool_keyboards = [{i:False for i in set(tune)} for j in range(0, num_keyboards)]
    # print(np.array(bool_keyboards).shape)
    for i in range(0, num_keyboards):
        for j in range(1, len(keyboards[i])):
            bool_keyboards[i][keyboards[i][j]] = True
    active_keyboards = [True for i in range(0, num_keyboards)]
    counter = 0
    for note in tune:
        available = 0
        for j in range(0, num_keyboards):
            if bool_keyboards[j][note] == False:
                active_keyboards[j] = False
            if active_keyboards[j] == True:
                available = available + 1
        if available == 0:
            counter = counter + 1
            for j in range(0, num_keyboards):
                if bool_keyboards[j][note] == True:
                    active_keyboards[j] = True
    return counter
args = read_input()
print(solve(*args))


