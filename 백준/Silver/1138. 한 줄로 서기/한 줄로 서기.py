# 1138 한 줄로 서기

# 아이디어
# 그리디일 것 같네요...

def find_left_position(target):
  result = []
  for i, number in enumerate(target):
    if number == 0:
      result.append(i)
  return result

def check_position(target, index):
  if index == 0:
    return 0
  else:
    count = 0
    for i in target[0:index]:
      if i == 0:
        count += 1
    return count
    

N = int(input())

left = list(map(int, input().split(" ")))

target = [0]*N

target[left[0]] = 1

for i in range(2, N+1):
  for index in find_left_position(target):
    if left[i-1] == check_position(target, index):
      target[index] = i
      break
  
  
for i in target:
  print(i, end=" ")