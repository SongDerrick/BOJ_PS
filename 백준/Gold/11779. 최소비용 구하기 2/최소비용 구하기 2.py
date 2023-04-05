# 11779 최소 비용 구하기

import heapq

INF = 1e10
N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]
path = [[] for _ in range(N + 1)]

for i in range(E):
  a, b, c = map(int, input().split(" "))
  graph[a].append([b, c])
  #graph[b].append([a, c])

v1, v2 = map(int, input().split(" "))
distance = [INF] * (N + 1)


def dijkstra(graph, start, distance):
  distance[start] = 0
  q = []
  heapq.heappush(q, [0, start])
  path[start] = -1

  while q:
    dist, ori = heapq.heappop(q)

    if distance[ori] < dist:
      continue

    for i in graph[ori]:
      cost = distance[ori] + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q, [cost, i[0]])
        path[i[0]] = ori


dijkstra(graph, v1, distance)
print(distance[v2])
idx = v2
result = [v2]

while True:
  temp = path[idx]
  
  if path[temp] == -1:
    result.append(temp)
    break
    
  result.append(temp)
  idx = temp
print(len(result))
for i in range(len(result)-1,-1,-1):
  print(result[i], end=" ")
