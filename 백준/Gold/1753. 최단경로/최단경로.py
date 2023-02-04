# 1753 최단경로
# 가중치가 부여된 그래프에서 최단 경로를 찾는 것이기 때문에 다익스트라로 접근해야 함..
# 방향성이 있는 가중치 그래프..
# 애초에 문제 이름 부터 최단 경로니까....
# 제한 시간이 1초이므로 개선된 다익스트라 => heapq을 사용해서 구현해봅시다

import heapq
import sys

input = sys.stdin.readline
INF = 1e9

V, E = map(int, input().split(" ")) # v는 정점, e는 간선
start = int(input()) # 시작 노드

graph = [[] for i in range(V+1)]

for _ in range(E):
  u, v, w = map(int, input().split(" "))
  # u 시작 -> v 도착점, w -> 가중치
  graph[u].append((v,w))

# 여기까지가 그래프를 그리는 단계...

# 이제는 distance 판단용 리스트
distance = [INF]*(V+1)


# 이제는 판단 용 우선순위 큐

q = []
heapq.heappush(q, (0, start)) # 첫번째 노드 큐에 입력
distance[start] = 0

while q:
  dist, ori = heapq.heappop(q)
  
  if distance[ori] < dist: # 이미 계산이 된 경우죠....
    continue 
    

  for i in graph[ori]:
    cost = distance[ori] + i[1]
    if distance[i[0]] > cost:
      distance[i[0]] = cost
      heapq.heappush(q, (distance[i[0]], i[0])) # distance, target
      # 이게 if 문 밖에 있을 필요가 없지 사실 최신화 된 노드만 push하면 되니까.


for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])
  
  
  