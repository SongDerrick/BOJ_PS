temp = []
temp = list(map(int, input().split(" ")))
#print(temp)
result = sum(x ** 2for x in temp)
print(result%10)