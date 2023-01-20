n = int(input())
temp = []

for i in range(n):
    k = int(input())
    if k == 0:
        temp.pop()
    else:
        temp.append(k)

        
print(sum(temp))