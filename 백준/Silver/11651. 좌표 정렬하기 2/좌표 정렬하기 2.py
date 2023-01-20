n = int(input())
temp = []

for i in range(n):
    x, y = map(int, input().split(" "))
    temp.append([x, y])

    
temp.sort(key = lambda x: (x[1], x[0]))

for i in range(n):
    print(str(temp[i][0]) + " " + str(temp[i][1]))