#11399
n = int(input())
result = 0
# n 명의 사람이 있다
# 돈을 인출하는데 걸리는 시간
time = list(map(int, input().split(" ")))

time.sort()

temp = time[0]

for i in range(1, n):
  result += temp
  temp = temp + time[i]

result += temp
print(result)