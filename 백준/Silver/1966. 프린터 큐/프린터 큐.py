# 1966
from collections import deque

case = int(input())
queue = deque()

result = []

for i in range(case):
    n, m = map(int, input().split(" "))
    temp = list(map(int, input().split(" ")))
    for j in range(len((temp))):
        queue.append([temp[j], j])
        
    count = 1
    #print(queue)
    while True:
        
        currMax = max(queue)[0]

        if len(queue) == 0:
            break
        elif queue[0][0] < currMax:
            queue.append(queue[0])
            queue.popleft()
        elif queue[0][0] == currMax:
            if queue[0][1] == m:
                result.append(count)
                break
            else:
                queue.popleft()
                count += 1
        else:
            break
        #print(queue)
        #print(max(queue))
        
    queue.clear()
#print(result)
for i in result:
    print(i)