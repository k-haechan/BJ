# 포도주 시식, 2024년 2월 19일 03:11:32, 31120kb, 432ms, 249b
n=int(input())
A=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=A[0]
if n>1:
    dp[1]=A[1]+A[0]
    if n>2:
        dp[2]=max(A[2]+A[0],A[2]+A[1],A[1]+A[0])
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-2]+A[i],dp[i-3]+A[i-1]+A[i])
print(dp[-1])
