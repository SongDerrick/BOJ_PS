# 7568 

n = int(input())
temp = []
for i in range(n):
    w, h = map(int, input().split(" "))
    temp.append([w,h,0])
    

for i in range(n):
    count = 1
    for j in range(n):
        if temp[i][0] < temp[j][0] and temp[i][1] < temp[j][1]:
            count += 1
    temp[i][2] = count    

for i in range(len(temp)):
    print(temp[i][2])

    