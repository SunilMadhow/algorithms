L = [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
total = 6
for i in range(1, len(L)):
	if L[i] == 0 and L[i - 1] == 0:
		total = total * 3
	if L[i] == 0 and L[i - 1] == 1:
		total = total * 4
	if L[i] == 1 and L[i - 1] == 0:
		total = total * 2

print(total)

