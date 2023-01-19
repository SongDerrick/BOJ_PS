# 1676
import math


n = int(input())
result = math.factorial(n)
count = 0

result = str(result)
#print(result)


for i in range(len(result)-1, -1, -1):
  if '0' == result[i]:
    count += 1
  else:
    break

print(count)