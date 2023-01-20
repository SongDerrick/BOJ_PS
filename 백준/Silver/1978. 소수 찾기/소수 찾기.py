n = int(input())

temp = []
count = 0

temp.extend(list(map(int, input().split(" "))))

for i in temp:
    for j in range(2,i+1):
        if i % j == 0:
            if j == i:
                count += 1
                break
            break
        else:
            continue
            
#print(temp)
print(count)