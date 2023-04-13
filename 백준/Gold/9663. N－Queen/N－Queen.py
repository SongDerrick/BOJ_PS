# 9663 N-Queen
import sys

sys.setrecursionlimit(10000)
answer = 0
board = [0] * 15


def check(cdx):
  for i in range(cdx):
    if board[cdx] == board[i] or abs(board[cdx] - board[i]) == (cdx - i):
      return False
      break

  return True


def nqueen(cdx):
  global answer
  if cdx == N:
    answer += 1
    return

  for i in range(N):
    board[cdx] = i
    if check(cdx):
      nqueen(cdx + 1)


N = int(input())
nqueen(0)
print(answer)
