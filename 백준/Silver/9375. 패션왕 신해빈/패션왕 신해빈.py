# 9375 패션왕 신해빈

import itertools

t = int(input())
result = []

for i in range(t):
  n = int(input())

  if n == 0:
    result.append(0)
  else:
    clothes = {}
    value = []
    answer = 0

    for i in range(n):
      cloth, type = input().split(" ")

      if type in clothes:
        clothes[type] += 1
      else:
        clothes[type] = 1

    r = 1
    for count in clothes.values():
      r *= count + 1
    r -= 1
    result.append(r)

for i in result:
  print(i)