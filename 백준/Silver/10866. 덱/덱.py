#10866 deque


from collections import deque
n = int(input())
temp = []
queue = deque([])


for i in range(n):
    order = input().split(" ")
    temp.append(order)
    
#print(temp)
for i in range(n):
    if temp[i][0] == 'push_back':
        queue.append(temp[i][1])
    elif temp[i][0] == 'push_front':
        queue.appendleft(temp[i][1])
    elif temp[i][0] == 'pop_front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.popleft())
    elif temp[i][0] == 'pop_back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.pop())
    elif temp[i][0] == 'size':
        print(len(queue))
    elif temp[i][0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif temp[i][0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif temp[i][0] == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
            
            