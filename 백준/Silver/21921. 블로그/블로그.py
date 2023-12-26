# 21921 blog
import sys

N, X = map(int, sys.stdin.readline().split())

visitors = list(map(int, sys.stdin.readline().split()))

window = []

# for i in range(N - X + 1):
#   window.append(sum(visitors[i:i + X]))

if (max(visitors) == 0):
  print('SAD')
else:
  tempResult = sum(visitors[:X])
  tempMax = tempResult
  count = 1

  for i in range(X, N):
    tempResult = tempResult - visitors[i - X] + visitors[i]
    if tempResult > tempMax:
      count = 1
      tempMax = tempResult
    elif tempResult == tempMax:
      count += 1

  print(tempMax)
  print(count)
