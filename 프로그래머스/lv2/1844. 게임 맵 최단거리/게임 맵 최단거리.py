from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    
    n = len(maps) # y 갯수
    m = len(maps[0]) # x 갯수
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = -1
            elif maps[i][j] == 1:
                maps[i][j] = 0
                
    #print(maps)
    
    q = deque([])
    q.append([0,0])
    
    while q:
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #print(q)
            
            if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
                continue
                    
            if maps[ny][nx] == -1:
                continue
                
            if maps[ny][nx] == 0 or maps[ny][nx] > maps[y][x] + 1:
                #print(nx, ny)
                maps[ny][nx] = maps[y][x] + 1
                q.append([nx, ny])
                
    if maps[n-1][m-1] == 0:
        answer = -1
    else:
        answer = maps[n-1][m-1] + 1
        
    
    return answer