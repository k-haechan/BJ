# 계단 오르기, 2024년 2월 18일 20:21:16, 31120kb, 48ms, 232b
n=int(input())
A=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=A[0]
if n>1:
    dp[1]=A[0]+A[1]
    if n>2:
        dp[2]=max(A[0]+A[2],A[1]+A[2])
for i in range(3,n):
    dp[i]=max(dp[i-3]+A[i-1]+A[i],dp[i-2]+A[i])
print(dp[n-1])
