n, c = map(int, input().split(" "))
temp = []
for _ in range(n):
    temp.append(int(input()))
    
temp.sort()

# 여기까지 sorting 완료

start = 1
end = temp[-1] - temp[0]
#print(start, end)
#print(temp)

while start <= end:
    
    standard = 0
    count = 1
    mid = (start+end) // 2
    #print(start, end)
    
    for i in range(n):
        if temp[i] - temp[standard] >= mid:
            count += 1
            standard = i
            
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
           
    result = (start+end)//2
    
print(result)