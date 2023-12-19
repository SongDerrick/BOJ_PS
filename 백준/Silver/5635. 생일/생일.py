# 5635 생일

T = int(input())

result = []
for _ in range(T):
  name, day, month, year = input().split(" ")
  result.append([int(year), int(month), int(day), name])

result.sort()

print(result[-1][3])
print(result[0][3])
