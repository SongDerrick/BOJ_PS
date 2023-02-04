# 11286 절대값 힙

# 힙을 만들 건데 튜플 형식으로 min heap을 구성하면 절댓값 판단이 될 듯하다...!

import heapq

n = int(input())
t = []
final = []

for i in range(n):
  temp = int(input())
  if temp == 0:
    if len(t) == 0:
      final.append('0')
    else:
      j, r = heapq.heappop(t)
      final.append(r)
  else:
    heapq.heappush(t, (abs(temp), temp))

for i in final:
  print(i)
