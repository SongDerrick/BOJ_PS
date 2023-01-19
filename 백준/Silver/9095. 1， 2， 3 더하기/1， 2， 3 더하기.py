t = int(input())

result =[0]*11
result[0] = 1
result[1] = 1
result[2] = 2
final = []

for i in range(3, 11):
  result[i] = result[i-3] + result[i-2] + result[i-1]

for i in range(t):
  temp = int(input())
  final.append(result[temp])

for i in final:
  print(i)