```python  
# 방향(0:남, 1: 동), 꺾기 가능 여부(0: 불가, 1:가능)
# 남을 바라보고있고 꺾기가 불가능하다는 의미는, 이전에서 꺾었다는 소리임
mod = 100000
w,h = map(int,input().split())

dp = [ [[[0]*2 for _ in range(2)] for _ in range(w+1)] for _ in range(h+1) ]

for i in range(1,h+1):
    dp[i][1][0][1] = 1
for i in range(1,w+1):
    dp[1][i][1][1] = 1

for i in range(2,h+1):
    for j in range(2,w+1):
        dp[i][j][0][0] = dp[i-1][j][1][1] 

        #남을 바라보고 있고 꺾기가 가능한 경우 ( 꺾기가능 + 꺽기불가능이 모두 가능하다 )
        dp[i][j][0][1] = (dp[i-1][j][0][1] + dp[i-1][j][0][0])%mod

        dp[i][j][1][0] = dp[i][j-1][0][1]
        dp[i][j][1][1] = (dp[i][j-1][1][0]+dp[i][j-1][1][1])%mod
print( (sum(dp[h][w][0])+ sum(dp[h][w][1]))%mod)

```
4차원 배열에 익숙해지기
