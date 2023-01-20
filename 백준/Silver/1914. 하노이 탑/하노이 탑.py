count = 0

def hanoi(n, source, destination, spare):
    global count
    if n == 1:
        temp.append([source, destination])
        count += 1
    else:
        hanoi(n-1, source, spare, destination)
        temp.append([source, destination])
        count += 1
        hanoi(n-1, spare, destination, source)
    
    
    
temp = [] 
n = int(input())
if n <= 20:
    hanoi(n, "1", "3", "2")
    print(count)
    for i in range(len(temp)):
        print(temp[i][0] + " " + temp[i][1])
else:
    print(2 ** n-1)