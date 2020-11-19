start =  input().split(" ")
N = int(start[0])
k = int(start[1])
inp = [[0,0]]
for i in range(0, N):
	col = input().split(" ")
	inp.append([int(col[0]), int(col[1])])
input()

dp = [[[None]*3 for i in range(0, k + 1)] for j in range(0, N+1)]

dp[0][0][0] = 0
dp[0][0][1] = 0
dp[0][0][2] = 0

for i in range(1, k + 1):
	for j in range(0, 3):
		dp[0][i][j] = -400*101

def solve(n, i, k):
	if dp[n][k][i] != None:
		return dp[n][k][i]
	else:
		v1 = inp[n][0]
		v2 = inp[n][1]
		ans = []
		if i == 0: #either ftbc
			ans = max([solve(n - 1, 0, k) + v1 + v2, solve(n - 1, 1, max(k - 1, 0)) + v2, solve(n-1, 2, max(k - 1, 0)) + v1])
		if i == 1: #1 ftbc
			ans = max([solve(n - 1, 0, k) + v1 + v2, solve(n - 1, 1, max(k - 1, 0)) + v2])
		if i == 2: #2 ftbc
			ans = max([solve(n - 1, 0, k) + v1 + v2, solve(n - 1, 2, max(k - 1, 0)) + v1])
	dp[n][k][i] = ans
	return ans

print(solve(N, 0, k))
