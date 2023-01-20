n = int(input())
temp = []

for i in range(n):
    k = input()
    temp.append([len(k),k])
    

temp.sort()    
#print(temp)


for i in range(n):
    if i == 0:
        print(temp[i][1])
    else:
        if temp[i-1][1] == temp[i][1]:
            continue
        else:
            print(temp[i][1])