# 10448 유레카 이론

import math

T = int(input())

numbers = []

for _ in range(T):
  numbers.append(int(input()))


def samGaksu(n):
  return int(n * (n + 1) / 2)


def Eureka(n):
  # print(int(math.sqrt(2*n)))
  limit = int(math.sqrt(2 * n))
  for i in range(limit, 0, -1):
    for j in range(limit, 0, -1):
      for k in range(limit, 0, -1):
        # print(samGaksu(i), samGaksu(j), samGaksu(k))
        if (samGaksu(i) + samGaksu(j) + samGaksu(k) == n):
          return 1

  return 0


for i in numbers:
  print(Eureka(i))
