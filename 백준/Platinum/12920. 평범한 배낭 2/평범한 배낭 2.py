N, M = map(int, input().split())

dp = [0 for _ in range(M+1)]
weight, satisfaction = [], []
for _ in range(N):
    V, C, K = map(int, input().split())

    idx = 1
    while K > 0:
        tmp = min(idx, K)

        weight.append(V * tmp)
        satisfaction.append(C * tmp)

        idx *= 2
        K -= tmp

for i in range(len(weight)):
    for j in range(M, 0, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + satisfaction[i])

print(dp[M])