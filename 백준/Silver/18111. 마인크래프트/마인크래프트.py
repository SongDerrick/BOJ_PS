# 18111 
n, m, b = map(int, input().split(" "))


temp = []

for i in range(n):
    t = list(map(int, input().split(" ")))
    temp.append(t)
              

# 맥시멈 높이랑 미니멈 높이랑 찾아서 비교해봄 맥시멈에 맞추는 거지...
# => 시간 구하기

# 맥시멈 높이에서 하나씩 줄여나가는 거임.... 
# 인벤토리 채우는 걸로 미니멈 높이 메꾸기

currMax = (max(max(temp)))
currMin = (min(min(temp)))
result = []
orgblock = b

for k in range(currMax, currMin-1, -1):

    count1 = 0
    count2 = 0
    b = orgblock

    for i in range(n):
        for j in range(m):
            s = temp[i][j] - k
            if temp[i][j] > k:
               
                count1 += s
                b += s
            elif temp[i][j] < k:
                count2 += -s
                b -= -s
                #print(b)

    if b >= 0:
        result.append([count1*2 + count2, k])

#print(result)        
result.sort(key = lambda x: (x[0], -x[1]))  
print(result[0][0],end=" ")
print(result[0][1])