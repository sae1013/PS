# 문제접근: 유령의 흔적을 시간으로 남긴다.
# 각 시간판에는, 유령이 도달한 시간을 기록한다.
# 유저를 BFS로 이동시킨다.
# 유령시간 < 유저시간 이면 이동하지못하고
# 유령시간 > 유저시간 이면 이동할 수 있다.
# 탈출할 수 있는지 살핀다.
# Time Complexity : O(NM)
```python
from collections import deque
import sys

def bfs_G(q,visit):
    while q :
        y,x = q.popleft() 
        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy+y 
            nx = dx+x 
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0 :
                q.append([ny,nx])
                visit[ny][nx] = visit[y][x] + 1 
                
def bfs_N(q,visit):
    while q :
        y,x = q.popleft() 
        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy+y 
            nx = dx+x 
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0 and board[ny][nx] in ['D','.']:
                q.append([ny,nx])
                visit[ny][nx] = visit[y][x] + 1
                    
    
n,m = map(int,input().split())
board = [input() for _ in range(n)]
visit_G = [[0]*m for _ in range(n)]
visit_N = [[0]*m for _ in range(n)]

q_N = deque() # 남우의 큐
q_G = deque() # 유령의 큐
ans_y,ans_x = 0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            ans_y,ans_x = i,j
        elif board[i][j] == 'N':
            q_N.append([i,j])
            visit_N[i][j] = 1
        elif board[i][j] == 'G':
            q_G.append([i,j])
            visit_G[i][j] = 1
bfs_G(q_G,visit_G) # 유령을 먼저 채운다.
bfs_N(q_N,visit_N)

if visit_N[ans_y][ans_x] > 0 and (visit_G[ans_y][ans_x] == 0 or visit_N[ans_y][ans_x] < visit_G[ans_y][ans_x]):
    print('Yes')
else: print('No')
```
