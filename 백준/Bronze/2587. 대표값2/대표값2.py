temp = []
for i in range(5):
    temp.append(int(input()))
    
temp.sort()
print(int(sum(temp)/5))
print(temp[2])
