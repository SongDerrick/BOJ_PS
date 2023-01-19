from collections import deque

n = int(input())

start, target = map(int, input().split(" "))

m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[start] = 1

for _ in range(m):
  s, t = map(int, input().split(" "))
  graph[s].append(t)
  graph[t].append(s)

cnt = -1
queue = deque([start])
while queue:
  v = queue.popleft()

  for i in graph[v]:

    if i == target:
      cnt = visited[v]
      break

    if visited[i] == 0:
      visited[i] = visited[v] + 1
      queue.append(i)


print(cnt)
