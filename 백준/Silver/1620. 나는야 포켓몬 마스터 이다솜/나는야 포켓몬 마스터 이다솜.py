n, m = map(int, input().split(" "))

pokemon1 = {} #딕셔너리 선언
pokemon2 = {}
result = []

for i in range(1,n+1):
  name = input()
  pokemon1[i] = name
  pokemon2[name] = i


for i in range(m):
  temp = input()
  if temp.isdecimal():
    result.append(pokemon1[int(temp)])
  else:
    result.append(pokemon2[temp])

for i in result:
    print(i)