i = input()
N = int(i)
def find(N,  start, end):
	n = end - start + 1
	# print("start = %d" %(start))
	# print("end = %d" %(end))
	# print("n = %d"%(n))
	a = start
	b = start + n // 2 - 1
	c = start + n // 4
	d = c + n//2 - 1
	if n == 3:
		a = start
		b = start + 1
		c = start + 1
		d = start + 2
	if n == 2:
		a = start
		b = start
		c = start + 1
		d = start + 1
	print("Q %d %d %d %d" %(a, b,c, d))
	i = input().split()
	x, y = int(i[0]), int(i[1])
	if x == 1 and y == 1 and c == b:
		print("A %d" % (c))
		return
	elif x == 1 and y == 0 and ((c - a) == 1 or b == a):
		print("A %d" % (a))
		return
	elif x == 0 and y == 1 and ((d - b) == 1 or d == c):
		print("A %d" % (d))
		return
	elif x == 0 and y == 0 and (end - d) == 1:
		print("A %d" % (end))
		return

	if x == 1 and y == 0:
		find(N, max(a - 1, 1), c)
	if y == 1 and x == 0:
		find(N,  b, min(d+1, N))
	if x == 0 and y == 0:
		find(N,  d, min(end + 1, N))
	if x == 1 and y == 1:
		find(N, c - 1, b + 1)


find(N, 1, N)