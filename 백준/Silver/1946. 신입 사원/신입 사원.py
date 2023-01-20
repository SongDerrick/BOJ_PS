import sys

t = int(sys.stdin.readline())
people = []
output = []

for _ in range(t):
    
    n = int(sys.stdin.readline())
    for i in range(n):
        r1, r2 = map(int, sys.stdin.readline().split(" "))
        people.append([r1, r2])
        
    people.sort()
    min = people[0][1]
    result = 1
    for j in range(1,n):
        if people[j][1] < min:
            min = people[j][1]
            result += 1
        
    output.append(result)
    people.clear()
        
    
for i in range(t):
    print(output[i])