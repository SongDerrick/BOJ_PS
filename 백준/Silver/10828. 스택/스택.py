#10828 stack


from collections import deque
n = int(input())
temp = []
queue = deque([])


for i in range(n):
    order = input().split(" ")
    temp.append(order)
    
#print(temp)
for i in range(n):
    if temp[i][0] == 'push':
        queue.append(temp[i][1])
    elif temp[i][0] == 'pop':
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
    elif temp[i][0] == 'top':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
            
            