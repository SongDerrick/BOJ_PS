# 1074번 Z 순회 문제
# 재귀 및 divide and conquer 문제라 할 수 있음
#

N, r, c = map(int, input().split(" "))
# r은 행 c는 열


def Z(N, r, c, result):
  # 네 가지의 케이스 + 베이스 케이스 존재
  curr = result
  if N == 1:  # 베이스 케이스
    # r,c는 0 혹은 1
    if r == 0 and c == 1:
      curr += 1
      print(curr)
    elif r == 1 and c == 0:
      curr += 2
      print(curr)
    elif r == 1 and c == 1:
      curr += 3
      print(curr)   
    else:
      print(curr)
  else:
    k = pow(2, N - 1) - 1  #
    if r <= k and c <= k:  # 왼 위 케이스
      Z(N - 1, r, c, curr)
    elif r <= k and c > k:  # 오른 위 케이스
      Z(N - 1, r, c - (k + 1), curr + pow(k + 1, 2))
    elif r > k and c <= k:  # 왼 아래 케이스
      Z(N - 1, r - (k + 1), c, curr + 2 * pow(k + 1, 2))
    else:  # 오른 아래 케이스
      Z(N - 1, r - (k + 1), c - (k + 1), curr + 3 * pow(k + 1, 2))



Z(N, r, c, 0)

