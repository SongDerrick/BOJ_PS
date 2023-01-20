
def check_chess(n):

    board1 = 'BWBWBWBWBW'
    board2 = 'WBWBWBWBWB'
    count1 = 0
    count2 = 0
    currMax = 0

    # 첫번째 케이스

    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if board1[j] == n[i][j]:
                    count1 += 1
        else:
            for j in range(8):
                if board2[j] == n[i][j]:
                    count1 += 1
                
    # 두번째 케이스

    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if board2[j] == n[i][j]:
                    count2 += 1
        else:
            for j in range(8):
                if board1[j] == n[i][j]:
                    count2 += 1

    currMax = max(count1, count2)
    return currMax


target = []
n, m = map(int, input().split(" "))
for i in range(n):
    target.append(input())
    
#print(target)
temp = []
result = 0

# 타깃 분할 해야함...
for i in range(0,n-7):
    for j in range(0,m-7):
        for k in range(0,8):
            temp.append(target[k + i][j:8+j])
        #print(check_chess(temp))
        #print(temp)
        result = max(result, check_chess(temp))
        temp.clear()

print(64 - result)