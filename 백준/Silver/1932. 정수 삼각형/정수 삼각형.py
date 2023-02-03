# 1912 정수 삼각형

n = int(input())
tri = [[0]*n for _ in range(n+1)]
dp = [[0]*n for _ in range(n+1)]



for i in range(1, n+1):
  tri[i] = (list(map(int, input().split(" "))))

dp[1][0] = tri[1][0]

for i in range(2, n+1):
  for j in range(i):
    if j == 0:
      dp[i][j] = dp[i-1][j] + tri[i][j]
    elif j == i-1:
      dp[i][j] = dp[i-1][j-1] + tri[i][j]
    else:
      dp[i][j] = max(dp[i-1][j] + tri[i][j], dp[i-1][j-1] + tri[i][j])
      
print(max(dp[n]))
    

  