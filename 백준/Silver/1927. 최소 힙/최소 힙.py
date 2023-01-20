# 1927 최소 힙

import heapq

n = int(input()) # 받을 숫자 갯수
target = [] # 얘로 우선 순위 큐 제작 ㅋ
result = [] # 출력 값

for _ in range(n):
  temp = int(input())
  if temp == 0: # 인풋이 0인 경우
    if not target: # 힙이 비어 있는 경우
      result.append(0)
    else: # 힙이 비어 있지 않은 경우
      result.append(heapq.heappop(target))
  else: # 인풋이 0이 아닌 경우
    heapq.heappush(target, temp)

for i in result:
  print(i)
