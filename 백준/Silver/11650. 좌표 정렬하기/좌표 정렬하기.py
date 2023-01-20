n = int(input())
array = []

for i in range(n):
    a, b = map(int, input().split(" "))
    array.append([a,b])
    
array.sort()
for i in range(len(array)):
    print(array[i][0], end=" ")
    print(array[i][1])