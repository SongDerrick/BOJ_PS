# 15650 N과 M
import itertools

N , M = map(int, input().split(" "))

temp = [i for i in range(1,N+1)]
#print(temp)

result = list(itertools.combinations(temp,M))

for i in result:
  for j in range(len(i)):
    print(i[j], end=" ")
  print()