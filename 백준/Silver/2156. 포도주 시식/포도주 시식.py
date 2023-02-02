# 2156 포도주 많이 먹기.... 시식회인데 적당히 먹어라 좀 ㅋㅋ

# 연속으로 3잔을 먹으면 안된다! 점화식을 찾아보자....
# n-1 과 n을 마시고 n-2는 안먹고 n-3까지의 최댓값을 구하자
# n-2와 n을 마시고 n-1은 안먹은 상태에서 

n = int(input())
cost = [0]
dp = [0]*10001
for _ in range(n):
  cost.append(int(input()))

if n == 1:
  dp[1] = cost[1]
elif n == 2:
  dp[1] = cost[1]
  dp[2] = cost[1] + cost[2]
else:
  #print(cost)
  dp[1] = cost[1]
  dp[2] = cost[1] + cost[2]
  dp[3] = max(cost[2] + cost[3], cost[3] + cost[1], dp[2])
  
  for i in range(4, n+1):
    dp[i] = max(cost[i-1] + cost[i] + dp[i-3], cost[i] + dp[i-2], dp[i-1])

print(dp[n])