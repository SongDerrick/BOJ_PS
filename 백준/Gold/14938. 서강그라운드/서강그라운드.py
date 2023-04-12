# 14938 서강그라운드

import heapq
INF = 1e9
n, m, r = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
item = [0]
item.extend(list(map(int, input().split(" "))))

for i in range(r):
  a, b, l = map(int, input().split(" ")) 
  graph[a].append([b, l])
  graph[b].append([a, l])

#print(graph)

def dijkstra(graph, start, distance):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, ori = heapq.heappop(q)

    if distance[ori] < dist:
      continue

    for i in graph[ori]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

result = []
for i in range(1, n+1):
  distance = [INF]*(n+1)
  dijkstra(graph, i, distance)
  #print(distance)
  totitem = 0
  for i in range(1, n+1):
    if distance[i] <= m:
      totitem += item[i]
  result.append(totitem)

print(max(result))

  
  
    