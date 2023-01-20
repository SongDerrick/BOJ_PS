import math

n = int(input())

temp=[]
out=[]
count = 1

for i in range(n):
    temp.append(int(input()))
    
print(round(sum(temp)/n)) # 산술평균

temp.sort()

print(temp[n//2]) #중앙값

# 최빈값만 구하면 댐....

result = []

for j in range(-4000,4001):
    result.append([j,0])
for i in range(n):
    result[temp[i]+ 4000][1] += 1
    
result.sort(key = lambda x : (x[1], -x[0]))

#print(result)

if result[-1][1] == result[-2][1]:
    print(result[-2][0])
else:
    print(result[-1][0])
print(temp[-1]-temp[0]) # 범위