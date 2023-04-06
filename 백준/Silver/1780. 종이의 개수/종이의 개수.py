import sys


def check(N, board, sx, sy):
    val = board[sy][sx]
    for y in range(sy, sy + N):
        for x in range(sx, sx + N):
            if val != board[y][x]:
                return False
    return True


def recursion(N, board, answer, sx, sy):
    if N == 1:
        answer[board[sy][sx] + 1] += 1
        return

    if check(N, board, sx, sy):
        answer[board[sy][sx] + 1] += 1
        return

    nn = N // 3
    for y in range(sy, sy + N, nn):
        for x in range(sx, sx + N, nn):
            recursion(nn, board, answer, x, y)


def solution(N, board):
    answer = [0, 0, 0]
    recursion(N, board, answer, 0, 0)
    return answer


IN = int(sys.stdin.readline())
IBoard = [list(map(int, sys.stdin.readline().split())) for _ in range(IN)]
OAnswer = solution(IN, IBoard)
for OAns in OAnswer:
    print(OAns)
