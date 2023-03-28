def solution(triangle):
    depth = len(triangle)
    dp = [[0]*depth for _ in range(depth)]
    dp[0][0] = triangle[0][0] # 첫 값은 미리 설정
    
    for i in range(1, depth):
        for j in range(i+1):
            if j == 0:
                curMax = dp[i-1][j]
            elif j == i:
                curMax = dp[i-1][j-1]
            else:
                curMax = max(dp[i-1][j-1], dp[i-1][j])
            # print(curMax)
            dp[i][j] += curMax + triangle[i][j]

    # print(dp)
    answer = max(dp[depth-1])
    return answer