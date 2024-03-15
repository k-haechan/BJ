# 이친수, 2023년 8월 7일 17:17:49, 31256kb, 52ms, 96b
N=int(input())
dp=[0]*(91)
dp[1]=1
for i in range(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N])
