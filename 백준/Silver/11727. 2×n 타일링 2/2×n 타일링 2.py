# 11727 2 x n 타일링


n = int(input())

dp = [0]*(1001)
#print(dp)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]*2

#print(dp)
print(dp[n]%10007)

