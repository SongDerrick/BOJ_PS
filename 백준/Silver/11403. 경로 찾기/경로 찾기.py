# 11403 경로 찾기
import heapq

INF = 10e9
N = int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(1, N + 1):
  temp = list(map(int, input().split(" ")))

  for idx, j in enumerate(temp):

    if i == idx + 1:
      continue

    if j == 1:
      graph[i].append(idx + 1)
      #graph[idx + 1].append(i)

#print(graph)


def dijkstra(graph, distance, start):
  #distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, ori = heapq.heappop(q)

    if dist > distance[ori]:
      continue

    for i in graph[ori]:
      #print(i)
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))


for i in range(1, N + 1):

  distance = [INF] * (N + 1)
  dijkstra(graph, distance, i)
  #print(distance)

  #print(distance)
  for j in range(1, N + 1):
    if distance[j] != INF or distance[j] == 0:
      print('1', end=" ")
    else:
      print('0', end=" ")

  print()
