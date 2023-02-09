# 1238 파티
import sys
from collections import deque

INF = 1e9
input = sys.stdin.readline

N, M, X = map(int, input().split(" "))
# N -> 도시 및 학생의 수, M ->  단방향 도로들, X -> 파티가 열리는 곳...

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for i in range(M):
  A, B, T = map(int, input().split(" "))
  graph[A].append((B,T))

#print(graph)

# 다익스트라 어케 함
def dijkstra(start):
  q = deque([(0, start)])

  while q:
    dist, ori = q.popleft()

    if distance[ori] > dist:
      distance[ori] = dist
    

    for i in graph[ori]:
      cost = distance[ori] + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        q.append((cost, i[0]))


dijkstra(X)
student = distance.copy()
#print(distance)
student[0] = 0

for i in range(1, N+1):
  distance = [INF]*(N+1)
  dijkstra(i)
  student[i] += distance[X]


print(max(student))
        