# 2178 미로 탐색
# bfs 문제 with 좌표 노드가 아닌 좌표다... 최단거리 문제므로 bfs를 사용.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

N, M = map(int, input().split(" "))
for _ in range(N):
  temp = list(input())
  graph.append(list(map(int, temp)))

# 0,0 이 1,1과 같은 방식의 그래프를 생성..

def bfs(x, y):
  q = deque([[x,y]])

  while q:

    x1, y1 = q.popleft()

    for i in range(4):
      nx = x1 + dx[i]
      ny = y1 + dy[i]

      if nx < 0 or ny < 0 or nx > M-1 or ny > N-1:
        continue

      if graph[ny][nx] == 0:
        continue

      if graph[ny][nx] == 1:
        graph[ny][nx] = graph[y1][x1] + 1
        q.append([nx, ny])
    


bfs(0,0)
print(graph[N-1][M-1])