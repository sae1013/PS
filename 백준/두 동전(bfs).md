BFS 응용문제들이 풀기 재밌다. 
시간복잡도: O(4**10) 

```python
from collections import deque

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
q = deque()

start = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'o':
            start.append(i)
            start.append(j)

q.append([start[0], start[1], start[2], start[3], 0])  # 두 동전의 위치, depth를 넣는다

while q:
    y1, x1, y2, x2, depth = q.popleft()
    if depth >= 10:
        print(-1)
        exit()
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny1, nx1 = dy + y1, dx + x1
        ny2, nx2 = dy + y2, dx + x2


        if not(0 <= ny1 < N and 0 <= nx1 < M) and not(0 <= ny2 < N and 0 <= nx2 < M):
            continue

        if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M:
            if grid[ny1][nx1] == '.' and grid[ny2][nx2] == '.':
                q.append([ny1, nx1, ny2, nx2, depth + 1])
            elif grid[ny1][nx1] == '.' and grid[ny2][nx2] !='.':
                q.append([ny1, nx1, y2, x2, depth + 1])
            elif grid[ny1][nx1] != '.' and grid[ny2][nx2] =='.':
                q.append([y1, x1, ny2, nx2, depth + 1])
        else:
            if depth+1 <= 10 :
                print(depth+1)
                exit()
            else:
                print(-1)
                exit()
print(-1)


```
