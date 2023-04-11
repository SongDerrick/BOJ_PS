# 11053 가장 긴 증가하는 부분 수열

n = int(input())
target = []
dp = [1] * n

target = list(map(int, input().split(" ")))

temp = target[0]
for i in range(1, n):
  for j in range(i):
    if target[i] > target[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
