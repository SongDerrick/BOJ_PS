# 7562 나이트의 이동

from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(graph, start, I, dest):
  q = deque([start])
  graph[start[1]][start[0]] = 0

  while q:
    x, y = q.popleft()

    if dest[0] == x and dest[1] == y:
      break

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx > I - 1 or ny > I - 1:
        continue

      if graph[ny][nx] > graph[y][x] + 1 or graph[ny][nx] == -1:
        graph[ny][nx] = graph[y][x] + 1
        q.append([nx, ny])


t = int(input())
result = []

for i in range(t):
  I = int(input())
  start = list(map(int, input().split(" ")))
  #print(start)
  dest = list(map(int, input().split(" ")))
  #print(dest)
  graph = [[-1] * I for _ in range(I)]
  bfs(graph, start, I, dest)
  #print(graph)
  #print(graph[dest[1]][dest[0]])
  #result.append()
  # for j in graph:
  #   print(j)
  print(graph[dest[1]][dest[0]])

# for i in result:
#   print(i)
