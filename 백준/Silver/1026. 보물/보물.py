# 1026 보물
N = int(input())
S = 0

A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
#print(A, B)
B.sort()
A.sort(reverse=True)

for i in range(N):
  S += A[i] * B[i]


print(S)
         
