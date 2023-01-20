from collections import deque

n, k = map(int, input().split(" "))

result = deque()
final = []

for i in range(1,n+1):
    result.append(i)
    
#print(result)

if n == 1:
    print('<',end="")
    for i in range(len(result)):
        print(result[i], end="")
    print('>')

for i in range(n-1):
    for j in range(k-1):
        temp = result.popleft()
        result.append(temp)
    final.append(result.popleft())
    if i == n-2:
        final.append(result.popleft())

        
for i in range(len(final)):
    if i == 0:
        print('<' + str(final[i])+ ", ", end="")
    elif i == len(final) - 1:
        print(str(final[i]) + '>')
    else:
        print(str(final[i]) + ", ", end="")