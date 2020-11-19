i = input()
N = int(i)
x = list(range(0, N+1))
def find(n, l, x):
	# print(n)
	# print(l)
	a = 1
	b = n // 2
	c = n // 4 + 1
	d = c + n//2 - 1
	if n == 3:
		a = 1
		b = 2
		c = 2
		d = 3
	if n == 2:
		a = 1
		b = 1
		c = 2
		d = 2
	print("Q %d %d %d %d" %(l[a], l[b], l[c], l[d]))
	i = input().split()
	x, y = int(i[0]), int(i[1])
	if x == 1 and y == 1 and c == b:
		print("A %d" % (l[c]))
		return
	elif x == 1 and y == 0 and (c - a) == 1 or b == a:
		print("A %d" % (l[a]))
		return
	elif x == 0 and y == 1 and (d - b) == 1 or d == c:
		print("A %d" % (l[d]))
		return
	elif x == 0 and y == 0 and (n - d) == 1:
		print("A %d" % (l[n]))
		return
	if x == 1 and y == 0:
		find(c - a + 2, l[a - 1:c+2], x)
	if y == 1 and x == 0:
		find(d - b + 2, l[b - 2:d+2], x)
	if x == 0 and y == 0:
		find(n - d + 1, l[d - 1:n+1], x)
	if x == 1 and y == 1:
		find(b - c + 3, l[c - 1 - 1: b + 2], x)


find(N, l, x)