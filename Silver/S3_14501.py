# 퇴사, 2023년 8월 7일 18:10:48, 31256kb, 44ms, 186b
N = int(input())

dp=[0]*(N+1)
for i in range(N):
    T,P = list(map(int,input().split()))
    dp[i+1]=max(dp[i],dp[i+1])
    if i+T<=N:
        dp[i+T]=max(dp[i+T],dp[i]+P)
print(dp[N])
