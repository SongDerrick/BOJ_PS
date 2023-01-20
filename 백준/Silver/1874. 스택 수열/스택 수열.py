#1874

from collections import deque

stack = deque()
result = []
count = 1
errorflag = True

n = int(input())


for i in range(n):
    k = int(input())
    
    # Stack이 빈경우, 채워줌
    if len(stack) == 0:
        while True:
            stack.append(count)
            result.append("+")
            
            if count == k:
                count += 1
                break
            else:
                count += 1
            
    if stack[-1] == k:
        stack.pop()
        result.append("-")
    elif stack[-1] < k:
        while True:
            stack.append(count)
            count += 1
            result.append("+")
        
            if stack[-1] == k:
                stack.pop()
                result.append('-')
                break
    else:
        errorflag = False


        
if errorflag == True:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")