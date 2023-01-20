# 1654

k,n = map(int, input().split(" "))
temp = []

for i in range(k):
    temp.append(int(input()))
    
temp.sort()

# 여기까지 정렬 완.. 이후부턴 이진 탐색

start = 1
end = max(temp)

while(start <= end):
    
    tot = 0
    mid = (start+end)//2 # 중간 지점을 정해줌
    
    for i in range(len(temp)):
        tot = tot + temp[i] // mid
            
    if tot >= n:
        start = mid + 1
    else:
        end = mid - 1
    
    #print(start, mid, end)


print(end)