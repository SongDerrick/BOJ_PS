# 9251 LCS

s1 = input()
s2 = input()

n = len(s1)
m = len(s2)
dp = [[0]*(n+1) for _ in range(m+1)]
#print(dp)

# tabulation approach

def lcs(x,y,n,m):

  for i in range(n+1): # 첫 인풋의 길이 6
    for j in range(m+1): # 두 번째 인풋의 길이 5
      if i == 0 or j == 0:
        dp[j][i] == 0
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if x[i-1] == y[j-1]:
        dp[j][i] = 1 + dp[j-1][i-1]
      else:
        dp[j][i] = max(dp[j][i-1], dp[j-1][i])


  return dp[m][n]

print(lcs(s1, s2, n,m))
#print(dp)
        