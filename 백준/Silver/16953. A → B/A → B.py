# 16853 A -> B

from collections import deque

A, B = map(int, input().split(" "))

graph = deque()
graph.append((B, 1))
count = 2

while B >= A:

  if B % 10 == 1:
    graph.append((B // 10, count))
    B = B // 10
    count += 1
  elif B % 2 == 0:
    graph.append((B // 2, count))
    B = B // 2
    count += 1
  else: 
    break


answerflag = False
result = 0
while graph:
  temp, currcount = graph.popleft()

  if temp == A:
    answerflag = True
    result = currcount
    break


if answerflag:
  print(result)
else:
  print(-1)
