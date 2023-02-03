# 1931 회의실 배정

n = int(input())

time = []

for _ in range(n):
  temp = list(map(int, input().split(" ")))
  time.append(temp)

#print(time)

time.sort(key = lambda x : (x[1], x[0]))
count = 1
curr = time[0][1]

for i in range(1, n):
  if curr <= time[i][0]:  
    curr = time[i][1]
    count += 1

print(count)
  