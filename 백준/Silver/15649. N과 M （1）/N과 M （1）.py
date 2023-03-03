# 15649 N과 M

import itertools

N, M = map(int, input().split(" "))
temp = []
for i in range(1, N + 1):
  temp.append(i)
result = list(itertools.permutations(temp, M))

for i in range(len(result)):
  for j in range(len(result[i])):
    print(result[i][j], end=" ")
  print()