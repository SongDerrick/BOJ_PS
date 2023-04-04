# 1504 특정한 최단 경로

import heapq

INF = 1e10
N, E = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]

if E > 0:
  for i in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split(" "))
distance = [INF] * (N + 1)


def dijkstra(graph, start, distance):
  distance[start] = 0
  q = []
  heapq.heappush(q, [0, start])

  while q:
    dist, ori = heapq.heappop(q)

    if distance[ori] < dist:
      continue

    for i in graph[ori]:
      cost = distance[ori] + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q, [cost, i[0]])


#print(graph)
dijkstra(graph, 1, distance)
temp = distance[v1]
distance = [INF] * (N + 1)
dijkstra(graph, v1, distance)
temp += distance[v2]
distance = [INF] * (N + 1)
dijkstra(graph, v2, distance)
temp += distance[N]

distance = [INF] * (N + 1)
dijkstra(graph, 1, distance)
temp1 = distance[v2]
distance = [INF] * (N + 1)
dijkstra(graph, v2, distance)
temp1 += distance[v1]
distance = [INF] * (N + 1)
dijkstra(graph, v1, distance)
temp1 += distance[N]

if v1 == v2:
  print('0')

elif temp >= INF or temp1 >= INF:
  print('-1')
else:
  print(min(temp, temp1))
