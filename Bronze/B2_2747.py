# 피보나치 수, 2024년 3월 3일 14:42:31, 31120kb, 44ms, 97b
n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
