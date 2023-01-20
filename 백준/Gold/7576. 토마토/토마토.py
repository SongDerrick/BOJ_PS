import sys
from collections import deque

def bfs(graph, pos):
    q = deque([(p[0], p[1]) for p in pos])
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == -1:
                continue

            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx, ny))

    return max(max(row) for row in graph) - 1

m, n = map(int, input().split())
tomatoes = []
for _ in range(n):
    tomatoes.append(list(map(int, sys.stdin.readline().rstrip().split())))

ripe_tomatoes = [(x, y) for y in range(n) for x in range(m) if tomatoes[y][x] == 1]

days = bfs(tomatoes, ripe_tomatoes)

if [0 for y in range(n) for x in range(m) if tomatoes[y][x] == 0]:
    print(-1)
else:
    print(days)