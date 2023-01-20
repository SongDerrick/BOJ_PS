# 18870 좌표 압축

# 처음 든 생각은 인풋이 백만개 이므로 O(N^2)로는 풀이가 불가능하다
# sort로는 어렵다
# heap으로도 어려워 보임...
# 딕셔너리? -> 소트 후 딕셔너리 -> O(NlogN)

import copy

n = int(input())
d = {}
count = 0
result = []
t = list(map(int,input().split(" ")))

final = copy.deepcopy(t)

t.sort()

for i in t:
  d[i] = 0

for i in d:
  if d[i] == 0:
    d[i] = count
    count += 1
  
for i in final:
  result.append(d[i])

for i in result:
  print(i, end=" ")