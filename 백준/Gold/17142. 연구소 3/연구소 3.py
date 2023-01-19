# 맞은 코드
from collections import deque

if __name__ == '__main__':
    N,M = map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    virus = []
    V = 0
    K=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                virus.append((i,j))
                V+=1
            elif arr[i][j]==0:
                K += 1
    ans =10**9

    def bfs(distance,res):
        global ans

        Q = deque()
        for r in res:
            Q.append(r)
            distance[r[0]][r[1]]=0
        t=infected=0

        while Q :
            idxs = Q.popleft()
            for dr, dc in (-1,0),(1,0),(0,1),(0,-1):
                nr = idxs[0] + dr
                nc = idxs[1] + dc
                if 0<=nr<N and 0<=nc<N and distance[nr][nc]==-1 and arr[nr][nc]!=1:
                    distance[nr][nc]=distance[idxs[0]][idxs[1]]+1
                    Q.append((nr, nc))
                    if arr[nr][nc]==0:
                        infected+=1
                        t = distance[nr][nc]

        # 다 퍼뜨린 후에는
        if K == infected:
            ans = min(ans, t)


    select = [False]*10

    def dfs(idx, cnt, V):
        if cnt == M:
            distance = [[-1] * N for _ in range(N)]
            res=[]
            for i in range(V):
                if select[i]:
                    res.append((virus[i][0],virus[i][1]))
            bfs(distance,res)
            return

        for i in range(idx, V):
            if not select[i]:
                select[i] = True
                dfs(i + 1, cnt + 1, V)
                select[i] = False

    dfs(0, 0, V)

    if ans == 10**9:
        print(-1)
    else:
        print(ans)