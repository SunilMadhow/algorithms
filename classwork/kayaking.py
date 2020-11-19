import sys
def read():
    data = sys.stdin.readlines()
    bne = [int(number) for number in data[0].split(" ")]
    s = [int(number) for number in data[1].split(" ")]
    k = [int(number) for number in data[2].split(" ")]
	# line_1 = input()
	# bne = [int(i) for i in line_1.split(" ")]
	# s = [int(i) for i in input().split(" ")]
	# k = [int(i) for i in input().split(" ")]
    return (bne, s, k)

def pairwise_speeds(s):
	d = {}
	d["bb"] = s[0] + s[0]
	d["bn"] = s[0] + s[1]
	d["be"] = s[2] + s[0]
	d["nn"] = s[1] + s[1]
	d["ne"] = s[1] + s[2]
	d["ee"] = s[2] + s[2]
	return d

def pair_up(bne, s):
	pairs = []
	pair_speeds = pairwise_speeds(s)
	while bne[0] > 0 and bne[2] > 0:
		bne[0] = bne[0] - 1
		bne [2] = bne[2] - 1
		pairs.append(pair_speeds["be"])
	if bne[0] > 0:
		while bne[0] > 0 and bne[1] > 0:
			bne[0] = bne[0] - 1
			bne [1] = bne[1] - 1
			pairs.append(pair_speeds["bn"])
		if bne[0] > 0:
			for i in range(0, bne[0]//2):
				pairs.append(pair_speeds["bb"])
		if bne[1] > 0:
			for i in range(0, bne[1]//2):
				pairs.append(pair_speeds["nn"])
	elif bne[2] >= 0:
		while bne[1] > 0 and bne[2] > 0:
			bne[1] = bne[1] - 1
			bne [2] = bne[2] - 1
			pairs.append(pair_speeds["ne"])
		if bne[1] > 0:
			for i in range(0, bne[1]//2):
				pairs.append(pair_speeds["nn"])
		if bne[2] > 0:
			for i in range(0, bne[2]//2):
				pairs.append(pair_speeds["ee"])


	return pairs

def pick_kayaks(pairs, kayaks):
	kayaks.sort(reverse = True)
	pairs.sort()
	speeds = []
	for i in range(0, len(pairs)):
		speeds.append(kayaks[i]*pairs[i])
	return min(speeds)

args = read()
pairs = pair_up(args[0], args[1])
print(pick_kayaks(pairs, args[2]))









# import random
# # def worstcase():
# 	kayak_speeds = [random.randint(1, 3) for i in range(0, 500000)]
# 	b = random.randint(0, 100000)
# 	n = random.randint(0, 100000 - b)
# 	e = random.randint(0, 100000 - n - b)
# 	print(b)
# 	print(n)
# 	print(e)
# 	print("---")
# 	s1 = random.randint(0, 1000)
# 	s2 = random.randint(s1, 1000)
# 	s3 = random.randint(s2, 1000)
# 	print(s1)
# 	print(s2)
# 	print(s3)
# 	print("-----")
# 	print(pick_kayaks(sorted(pair_up([b, n, e], [s1, s2, s3])), kayak_speeds))

# worstcase()

 