# 11404 플로이드 - 워셜


INF = 1e9
n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split(" "))
  graph[a].append((b,c))


#print(graph) # graph 그리기 끝


result = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
  for b in range(1, n+1):
    if a == b:
      result[a][b] = 0

# 플로이드 워셜 테이블 그려주고....

for a in range(1,n+1):
  for b in graph[a]:
    # b[0] : 도착 도시, b[1] : 거리
    if result[a][b[0]] > b[1]:
      result[a][b[0]] = b[1]
    

# 이제 3중 for 문으로 테이블을 채워주자...
for k in range(1,n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      result[a][b] = min(result[a][b], result[a][k] + result[k][b])

for i in range(1, n+1):
  for j in range(1, n+1):
    if result[i][j] == INF:
      print(0, end=" ")
    else:
      print(result[i][j], end=" ")
  print()
      