# 11726 2 x n 타일링

# 단순 그리디 인줄 알았는데... dp 문제였다..

# 세로 줄은 2 x 1 칸 
# 가로 줄은 1 x 2 칸

n = int(input())
tile = [[0]*(n+1) for _ in range(n+1)]
result = 0

for i in range(1,n+1):
  tile[0][i] = 1
  tile[i][0] = 1

for i in range(1, n+1): # 가로 축
  for j in range(1, n+1): # 세로 축
    tile[i][j] = tile[i-1][j] + tile[i][j-1]
  
#print(tile)

if n % 2 == 0:
  # 짝수 케이스
  for i in range(n//2, -1 , -1):
    result+= tile[i][n - 2*i]
  print(result%10007)
else:# 홀수 케이스
  for i in range((n-1)//2 , -1, -1):
    #print(tile[i][n - 2*i])
    result += tile[i][n - 2*i]
  print(result%10007)
  


