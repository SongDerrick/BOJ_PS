# 2667 단지번호 붙이기 
# 문제를 읽는 순간... 그래프의 DFS or BFS 임을 알 수 있었다.
# 주변이 모두 0인 노드만 나올 때 까지 탐색하면 댐!

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input()) # 정사각형의 갯수를 구함

graph = []
count = 0
result = []

for _ in range(n):
  graph.append(list(str(input())))

  
# 그래프 그리기 끝

def bfs(x, y):
  # '1' 이 나온 경우.. '2'-> visited 처리
  graph[y][x] = '0'
  q = deque([(x,y)])
  r = 0
  
  while q:
    x1, y1 = q.popleft()
    #print(x1,y1)
    r += 1
    
    for i in range(4):
      nx = x1 + dx[i]
      ny = y1 + dy[i]
      
      
      
      if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
        continue

      if graph[ny][nx] == '1':
        q.append((nx, ny))
        graph[ny][nx] = '0'



  return r

for i in range(n):
  for j in range(n):
    if graph[j][i] == '1':
      result.append(bfs(i,j))
      count += 1

result.sort()
print(count)
for i in result:
  print(i)

