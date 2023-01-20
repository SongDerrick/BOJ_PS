a, b = map(int, input().split(" "))
temp1 = []
temp2 = []
small = 0
big = 0

for i in range(1, a+1):
    if a % i == 0:
        temp1.append(i)
        
for i in range(1, b+1):
    if b % i == 0:
        temp2.append(i)

#print(temp1)
#print(temp2)

if len(temp1) <= len(temp2):
    for i in temp2:
        if i in temp1:
            #print(i)
            small = i
else:
    for i in temp1:
        if i in temp2:
            #print(i)
            small = i
            
print(small)
if len(temp1) <= len(temp2):
    print(int((a/small)*b))
else:
    print(int(a*(b/small)))