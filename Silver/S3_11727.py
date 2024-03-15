# 2×n 타일링 2, 2023년 8월 4일 12:00:59, 31388kb, 48ms, 135b
dp=[0]*1001
dp[0]=0
dp[1]=1
dp[2]=3

for i in range(3,1001):
    dp[i]=2*dp[i-2]+dp[i-1]

n=int(input()) # [1,1000]
print(dp[n]%10007)

