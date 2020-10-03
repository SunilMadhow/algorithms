from math import factorial
from fractions import gcd
import inspect
def partition(n): #returns integer partition to be used in counting cycles in the symmetric group S_n
    answer = set()
    answer.add((n, ))
    for x in range(1, n):
	    for y in partition(n - x):
	        answer.add(tuple(sorted((x, ) + y)))
    return answer

def get_partition(n): #get the partition in the format of a list (a_1, ... a_n) where a_i is the coefficient of the ith integer in the partition
    # print inspect.stack()[1][3]
    answer = list(partition(n))
    lst = []
    for i in answer: 
        l = [0]*n
        for j in range(1, n+1):
           l[j - 1]=i.count(j)
        lst.append((l, i)) #package them together, as both will be needed when the product group is formed
    return lst

def summand(a, b, w, h, s, order): #calculate each term within the summation of the cycle index equation
#using a result I don't understand regarding the cycle index of a direct-product group
	answ = order
	for i in range(1, w + 1):
		answ //= (i**a[0][i-1])*factorial(a[0][i-1])
	for j in range(1, h + 1):
		answ //= (j**b[0][j-1])*factorial(b[0][j-1])
	count = 0
	for i in a[1]:
		for j in b[1]:
			count = count + gcd(i, j)
	return answ*(s**count)


def polya(h, w, s):
	sum_ = 0
	group_order = factorial(h)*factorial(w)
	H = get_partition(h)
	W = get_partition(w)
	for b in H:
		for a in W:
			summand_ = summand(a, b, w, h, s, group_order)
			sum_ = sum_ + summand_
	return sum_/(group_order)

def solution(w, h, s):
	return polya(h, w, s)
