# 13549 숨바꼭질

from collections import deque

N, K = map(int, input().split(" "))

target = [-1] * 100001


def bfs(target, start):
  q = deque([start])
  target[start] = 0

  while q:
    cur = q.popleft()

    if 0 <= cur - 1 <= 100000:
      if target[cur - 1] == -1 or target[cur - 1] > target[cur] + 1:
        target[cur - 1] = target[cur] + 1
        q.append(cur - 1)

    if 0 <= cur + 1 <= 100000:
      if target[cur + 1] == -1 or target[cur + 1] > target[cur] + 1:
        target[cur + 1] = target[cur] + 1
        q.append(cur + 1)
    if 0 <= 2 * cur <= 100000:
      if target[2 * cur] == -1 or target[2 * cur] > target[cur]:
        target[2 * cur] = target[cur]
        q.append(2 * cur)


bfs(target, N)
print(target[K])
