n = int(input())

temp = []

for i in range(n):
    age, name = input().split(" ")
    temp.append([int(age), i, name])

temp.sort()
for i in range(n):
    print(temp[i][0], end=" ")
    print(temp[i][2])