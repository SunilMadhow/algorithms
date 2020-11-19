import sys
def read():
    data = sys.stdin.readlines()
    line_1 = data[0].split(" ")
    m = int(line_1[0])
    r = int(line_1[1])
    l = []
    for line in data[1:r+2]:
        l.append(int(line.strip()))
    print(l)
    return [m, l]

def solve(n, l):
	if len(l) == n:
		print("too late")
		return
	for i in range(1, n+1):
		if i not in l:
			print(i)
			return
args = read()
solve(*args)
