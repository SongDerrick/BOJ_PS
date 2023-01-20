import heapq

temp = []
result = []

n = int(input())

for i in range(n):
    t = int(input())
    if t == 0:
        if temp:
            result.append(heapq.heappop(temp)*-1)
        else:
            result.append(t)
    else:
        heapq.heappush(temp, -t)
    #print(temp)   

for i in result:
    print(i)
        