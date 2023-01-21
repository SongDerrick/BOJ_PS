# 17219 비밀번호 찾기

n, m = map(int, input().split(" "))

dict = {}
result = []

for _ in range(n):
  page, pw = map(str, input().split(" "))
  dict[page] = pw

for _ in range(m):
  target = input()
  result.append(dict[target])

for i in result:
  print(i)
  




