t = int(input())

fib = [[0]* 2 for i in range(41)]
fib[0][0] = 1
fib[0][1] = 0
fib[1][0] = 0
fib[1][1] = 1


for i in range(2,41):
    fib[i][0] = fib[i-1][0] + fib[i-2][0]
    fib[i][1] = fib[i-1][1] + fib[i-2][1]
    
result = []
for _ in range(t):
    temp = int(input())
    result.append([fib[temp][0], fib[temp][1]])

for i in range(len(result)):
    print(result[i][0], result[i][1])