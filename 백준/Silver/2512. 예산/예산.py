#2512

n = int(input())
temp = []
temp.extend(list(map(int, input().split(" "))))
yesan = int(input())

temp.sort()
start = 0
end = temp[-1]

while start <= end:
    tot = 0
    mid = (start + end) // 2
    
    for i in range(n):
        if temp[i] >= mid:
            tot += mid
        else:
            tot += temp[i]
            
    if yesan >= tot:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)