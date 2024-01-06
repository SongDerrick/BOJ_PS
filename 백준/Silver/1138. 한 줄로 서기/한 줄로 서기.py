# 1138 한 줄로 서기

# 아이디어
# 그리디일 것 같네요...

def find_left_position(target): # 들어갈 수 있는 남은 자리 인덱스 찾기
  result = []
  for i, number in enumerate(target):
    if number == 0:
      result.append(i)
  return result

def check_position(target, index): # 어떤 자리에 들어갔을 때 왼쪽에 큰 수가 몇개인지 체크
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

target[left[0]] = 1 # 첫 번째 사람은 위치를 바로 알 수 있음 -> 그리디 접근

for i in range(2, N+1): # 두 번쨰 사람부터 룹
  for index in find_left_position(target): # 남은 자리 중 에서 포문
    if left[i-1] == check_position(target, index): # 남은 자리에서 왼쪽에 큰 수 갯수 비교
      target[index] = i
      break # 맞는 경우 저장하고 브레잌
  
  
for i in target: # 답안 출력
  print(i, end=" ")