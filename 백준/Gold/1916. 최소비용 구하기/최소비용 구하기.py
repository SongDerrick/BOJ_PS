# 1916 최소비용 구하기
# 도시가 등장! 그리고 도시를 잇는 버스 노선의 등장 전형적인 방향성과 가중치가 있는 그래프다!
# 이말인 즉슨 -> 다익스트라

import heapq
import sys

input = sys.stdin.readline
INF = 1e9

V = int(input())
E = int(input())  # v는 정점, e는 간선

graph = [[] for i in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split(" "))
  # u 시작 -> v 도착점, w -> 가중치
  graph[u].append((v, w))

# 여기까지가 그래프를 그리는 단계...

# 이제는 distance 판단용 리스트
distance = [INF] * (V + 1)

start, dest = map(int, input().split(" "))

# 출발도시와 도착도시
# 이제는 판단 용 우선순위 큐

q = []
heapq.heappush(q, (0, start))  # 첫번째 노드 큐에 입력
distance[start] = 0

while q:
  dist, ori = heapq.heappop(q)

  if distance[ori] < dist:  # 이미 계산이 된 경우죠....
    continue

  for i in graph[ori]:
    cost = distance[ori] + i[1]
    if distance[i[0]] > cost:
      distance[i[0]] = cost
      heapq.heappush(q, (distance[i[0]], i[0]))  # distance, target
      # 이게 if 문 밖에 있을 필요가 없지 사실 최신화 된 노드만 push하면 되니까.

print(distance[dest])
