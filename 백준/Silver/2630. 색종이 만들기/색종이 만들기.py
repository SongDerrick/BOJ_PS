# 2630 색종이 만들기

# 재귀 스멜이 나는 문제다...
# 1,2,3,4 사분면으로 나눠서 재귀... 하는게 맞는 듯ㅎ함?
# 일단 함수에 전 2차원 배열을 넣고 4분면으로 분할일단 해버림..
# 만약에 사분면이 모두 0 이거나 1이면 재귀 금지 -> 색종이 카운트
# 나머지 케이스에서는 재귀 시켜 버림...
# 재귀 종료 베이스 케이스 1) 모두 0 or 1임 -> 사이즈가 1인 경우도 포함한 것임...
def color(target):
  global blue
  global white
  if target[0][0] == 1:
    blue += 1
  else:
    white += 1

def decide(target):
  if any(1 in t for t in target) and any(0 in t for t in target):
    #print("재귀 드가자")
    paper(target)
  else:
    #print("재귀 노 필요")
    color(target)

    
def paper(target):
  N = len(target[0])
  R = int(N/2)
  t1 = []
  t2 = []
  t3 = []
  t4 = []
  for i in range(R):
    t1.append(target[i][:R])
    t2.append(target[i][R:])
    t3.append(target[i+R][:R])
    t4.append(target[i+R][R:])

  #print(t1,t2,t3,t4)

  decide(t1)
  decide(t2)
  decide(t3)
  decide(t4)



blue = 0 
white = 0
    
n = int(input())
target = []
for i in range(n):
  target.append(list(map(int, input().split(" "))))

decide(target)
if blue != 0 or white != 0:
  print(white)
  print(blue)
else:
  paper(target)
  print(white)
  print(blue)