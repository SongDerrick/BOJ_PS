n, k = input().split(' ')
n = int(n)
target = int(k)
coin = []
count = 0

for i in range(n): # O(n)
    temp = int(input())
    coin.append(temp)

for i in range(n-1, -1, -1): # O(n^2)
    while True: 
        if target < coin[i]:
            break
        else:
            target = target - coin[i]
            count += 1
            
    if target == 0:
        break
        
print(count)