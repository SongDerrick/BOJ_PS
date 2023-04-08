# 1991 트리 순회

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
  n1, n2, n3 = input().split(" ")
  graph[ord(n1) - 65].append(n2)
  graph[ord(n1) - 65].append(n3)


def pretraverse(graph, start):
  idx = ord(start) - 65

  if start == '.':
    return
  print(start, end="")
  pretraverse(graph, graph[idx][0])
  pretraverse(graph, graph[idx][1])


def midtraverse(graph, start):
  idx = ord(start) - 65

  if start == '.':
    return
  midtraverse(graph, graph[idx][0])
  print(start, end="")
  midtraverse(graph, graph[idx][1])


def posttraverse(graph, start):
  idx = ord(start) - 65

  if start == '.':
    return
  posttraverse(graph, graph[idx][0])
  posttraverse(graph, graph[idx][1])
  print(start, end="")


pretraverse(graph, 'A')
print()
midtraverse(graph, 'A')
print()
posttraverse(graph, 'A')
