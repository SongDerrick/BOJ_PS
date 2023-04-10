# 3687 성냥개비
number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#         0  1  2  3  4  5  6  7  8  9

n = int(input())

dp = [0] * 101
dp[1] = -1
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6  # 나중에 예외 처리 요망
dp[7] = 8
dp[8] = 10

for i in range(9, 101):
  #print(str(dp[i - 7]) + str(dp[7]))
  #print(str(dp[i - 6]) + '0')
  dp[i] = min(int(str(dp[i - 7]) + str(dp[7])), int(str(dp[i - 6]) + '0'),
              int(str(dp[i - 5]) + '2'))

  #print(i, dp[i])
target = []

for i in range(n):
  target.append(int(input()))

for i in target:
  #print(i)
  a = dp[i]
  ans = ''
  if i % 2 == 1:
    ans += '7'
    for i in range(i // 2 - 1):
      ans += '1'
  else:
    for i in range(i // 2):
      ans += '1'
  print(a, ans)
