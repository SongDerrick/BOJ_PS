import sys
input = sys.stdin.readline

N = int(input())

num = [0] * 10000

for i in range(N):
    temp = int(input())
    num[temp-1] = num[temp-1] + 1

for i in range(10000):
    if num[i] != 0:
        for j in range(num[i]):
            print(i+1)