# 15686 치킨 배달

N, M = map(int, input().split(" "))

graph = []
chicken = []
home = []

for i in range(N):
  temp = list(map(int, input().split(" ")))
  for j in range(N):
    if temp[j] == 2:
      chicken.append([j, i])  # (x,y)
    elif temp[j] == 1:
      home.append([j, i])  # (x,y)
  graph.append(temp)

#print(graph)
#print(chicken)
#print(home)

result = [0] * M
final = []


def check(depth):
  if depth == 0:
    return True
  elif result[depth - 1] < result[depth]:
    return True
  else:
    return False


def recursion(depth):
  global result
  if depth == M:
    #print(result)
    tot = 0
    for i in home:
      #print(i)
      curMin = 10e9
      for j in result:
        #print(chicken[j])
        temp = abs(chicken[j][0] - i[0]) + abs(chicken[j][1] - i[1])
        if curMin > temp:
          curMin = temp
      tot += curMin
      #print(tot)
    final.append(tot)
    return

  for i in range(len(chicken)):
    result[depth] = i
    if check(depth):
      recursion(depth + 1)


recursion(0)
print(min(final))
