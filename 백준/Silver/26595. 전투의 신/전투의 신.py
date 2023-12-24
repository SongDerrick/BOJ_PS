# 26595 전투의 신

from heapq import heappush, heappop

N = int(input())

A, Pa, B, Pb = map(int, input().split(" "))

x = []
y = []

# Ax + By <= N

if Pa > Pb:
  pivot = Pa
else:
  pivot = Pb

index = N // pivot  # 17 // 4

while True:
  if index < 0:
    break

  if pivot == Pb:
    y.append(index)
    x.append((N - Pb * index) // Pa)
  else:
    x.append(index)
    y.append((N - Pa * index) // Pb)

  index -= 1

result = []

for i in range(len(x)):
  heappush(result, (-(A * x[i] + B * y[i]), i))

print(x[result[0][1]], y[result[0][1]])
