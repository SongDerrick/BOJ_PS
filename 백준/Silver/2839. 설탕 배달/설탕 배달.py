n = int(input())
result = 0

while True:
    
    if n < 0:
        result = -1
        break
    else:
        if n % 5 == 0:
            result = result + (n // 5)
            break
        else:
            result += 1
            n -= 3
print(result)