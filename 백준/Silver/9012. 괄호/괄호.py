from collections import deque
n = int(input())
result = []
stack = deque()

for i in range(n):
    temp = list(input())
    for i in range(len(temp)):
        if temp[i] == '(':
            stack.append(temp[i])
        else:
            if len(stack) == 0:
                stack.append(temp[i])
                break
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")
        stack.clear()

for i in range(len(result)):
    print(result[i])