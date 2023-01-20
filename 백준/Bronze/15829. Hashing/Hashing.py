# 15829

n = int(input())
s = input()
result = 0


for i in range(n):
    temp = (ord(s[i]) - 96)
    result = result + temp*(31**i)
    
h = result % 1234567891
    
print(h)