# 파도반 수열, 2024년 2월 18일 18:17:45, 31120kb, 48ms, 149b
dp=[0]*101
dp[1]=dp[2]=dp[3]=1
for i in range(4,101):
    dp[i]=dp[i-2]+dp[i-3]
T=int(input())
for _ in range(T):
    n=int(input())
    print(dp[n])
