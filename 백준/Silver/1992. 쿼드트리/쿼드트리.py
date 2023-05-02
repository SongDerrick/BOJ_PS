# 1992 쿼드트리

N = int(input())

graph = []
for i in range(N):
  temp = list(str(input()))
  temp = [int(i) for i in temp]
  graph.append(temp)

#print(graph)


def check(graph):
  pivot = graph[0][0]
  for i in graph:
    for j in i:
      if j != pivot:
        return False

  return True


def split(graph, N):
  graph1 = []
  graph2 = []
  graph3 = []
  graph4 = []
  for i in range(N // 2):
    graph1.append(graph[i][0:N // 2])
  for i in range(N // 2):
    graph2.append(graph[i][N // 2:N])
  for i in range(N // 2, N):
    graph3.append(graph[i][0:N // 2])
  for i in range(N // 2, N):
    graph4.append(graph[i][N // 2:N])

  #print(graph1, graph2, graph3, graph4)
  return graph1, graph2, graph3, graph4


def quadtree(graph, N):

  if check(graph):
    print(str(graph[0][0]), end="")
    return
  else:
    print("(", end="")
    graph1, graph2, graph3, graph4 = split(graph, N)
    quadtree(graph1, N // 2)
    if not check(graph1):
      print(")", end="")
    quadtree(graph2, N // 2)
    if not check(graph2):
      print(")", end="")
    quadtree(graph3, N // 2)
    if not check(graph3):
      print(")", end="")
    quadtree(graph4, N // 2)
    if not check(graph4):
      print(")", end="")

  #print(")", end="")

if N == 1 or check(graph):
  print(str(graph[0][0]))
else:
  quadtree(graph, N)
  print(")")
