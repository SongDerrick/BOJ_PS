result = []

while True:
    
    n = input()
    totlen = len(n)
    
    if n == '0':
        break
        
    if totlen == 1:
        result.append("yes")

# 홀수 케이스

    if totlen % 2 == 1:
        for i in range(0,totlen//2):
            if n[i] == n[totlen -1 -i]:
                if i == totlen//2 - 1:
                    result.append("yes")
                    break
            else:
                result.append("no")
                break
# 짝수 케이스
    else:
        for i in range(0,totlen//2):
            if n[i] == n[totlen -1 -i]:
                if i == totlen//2 - 1:
                    result.append("yes")
                    break
            else:
                result.append("no")
                break

for i in range(len(result)):
    print(result[i])
