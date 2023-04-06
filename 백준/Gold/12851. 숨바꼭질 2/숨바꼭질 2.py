# 12851 숨바꼭질 2

from collections import deque

N, K = map(int, input().split(" "))
INF = 1e10
visited = [INF] * 100001
path = []

def bfs(start, target, visited):
  visited[start] = 0
  q = deque([[start, '-']])
  while q:
    temp = q.popleft()
    s = temp[0]
    par = temp[1]
    #print("순회 시작", s)
    #print(q)
    path.append([s,par])

    sample = []

    sample.append(2 * s)
    sample.append(s - 1)
    sample.append(s + 1)

    for i in sample:
      if i >= 0 and i <= 100000 and visited[i] >= visited[s] + 1:
        visited[i] = visited[s] + 1
        q.append([i, s])

    #if target in sample:
    #  print(q)
    #  break


bfs(N, K, visited)
#print(visited)
print(visited[K])
path.sort()
#print(path)
result = 0

for i in path:
  if i[0] == K:
    result += 1

print(result)
  
