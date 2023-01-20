temp = []
temp2 = []

for i in range(3):
    temp.append(int(input()))
    
for i in range(2):
    temp2.append(int(input()))
    
print(min(temp) + min(temp2) - 50)