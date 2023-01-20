import sys

n = int(sys.stdin.readline())

temp = [] 

for i in range(n):
    temp.append(int(sys.stdin.readline()))
    
temp.sort()

for i in temp:
    print(i)