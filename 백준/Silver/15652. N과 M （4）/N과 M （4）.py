# 15652 N과 M(4)

N, M = map(int, input().split(" "))
result = [0]*M
target = [i for i in range(1,N+1)]

def check(depth, target):
  if depth == 0:
    return True
  elif result[depth-1] <= target:
    return True
  else:
    return False


def combination(depth):
  if depth == M:
    for i in result:
      print(i, end=" ")
    print()
    return

  for i in range(N):
    if check(depth, target[i]) is True:
      result[depth] = target[i]
      combination(depth + 1)
    
    

combination(0)
