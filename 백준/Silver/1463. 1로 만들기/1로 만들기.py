#1463

n = int(input())
result = 0

if n < 4:
    dp = [0]*4
else:
    dp = [0]*(n+1)

dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//3]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//2]+1)
    else:
        dp[i] = dp[i-1]+1
        
print(dp[n])
#print(dp)