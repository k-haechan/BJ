# 알고리즘 수업 - 피보나치 수 1, 2024년 2월 18일 16:46:04, 31120kb, 40ms, 121b
n=int(input())
dp=[0 for _ in range(n+1)]
dp[1]=dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n],n-2)
