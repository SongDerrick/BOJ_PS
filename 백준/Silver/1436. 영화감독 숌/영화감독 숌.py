#1436

n = int(input())
count = 0
result = 0
i = 0

while True:
    if '666' in str(i):
        count += 1
        result = i
    
    if count == n:
        break
        
    i += 1
print(result)