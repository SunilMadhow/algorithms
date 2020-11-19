def merge(arr, le, m, ri): #l and r are sorted
	displeasure_tuple = [0, 0]
	displeasure = 0

	l = arr[le:m+1]
	r = arr[m+1:ri+1]
	
	k = len(l) - 1
	i = l[k]
	p = len(r) - 1
	j = r[p]
	while True:
		j = r[p]
		while j < i:
			if (i - j) % 2 == 0:
				displeasure_tuple[0] += 1
			else:
				displeasure_tuple[1] += 1
			if k != 0:
				k -= 1
				i = l[k]
			else:
				break
		displeasure += (displeasure_tuple[0] + displeasure_tuple[1]*2)
		if p == 0:
			break
		p -= 1
		prev_j = j
		j = r[p]
		if (prev_j - j) % 2 == 1:
			displeasure_tuple[0], displeasure_tuple[1] = displeasure_tuple[1], displeasure_tuple[0]
	merge_sor(arr, l, r, le)
	return displeasure
	
def merge_sor(arr, l, r, le):
	i = j = k = 0
	while i < len(l) and j < len(r):
		if l[i] < r[j]:
			arr[k+le] = l[i]
			i += 1
		else:
			arr[k+le] = r[j]
			j += 1
		k = k + 1
	while i < len(l):
		arr[k+le] = l[i]
		k += 1
		i += 1
	while j < len(r):
		arr[k+le] = r[j]
		k += 1
		j += 1

def quantify(arr, l, r):
	d = 0
	if (l < r):
		m = (l + r)//2
		print((l, m, r))
		d += quantify(arr, l, m)
		d += quantify(arr, m+1, r)
		d += merge(arr, l, m, r)
	return d

arr = [3, 2, 1, 7, 6, 5, 4, 8, 9]
print(quantify(arr, 0, len(arr)-1))


