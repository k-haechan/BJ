# 쉬운 계단 수, 2024년 2월 19일 02:54:32, 31120kb, 40ms, 185b
n=int(input())
dp=[1]*10
dp[0]=0
for i in range(n-1):
    A=[0]*10
    A[0]=dp[1]
    for j in range(1,9):
        A[j]=dp[j-1]+dp[j+1]
    A[9]=dp[8]
    dp=A
print(sum(dp)%1000000000)
