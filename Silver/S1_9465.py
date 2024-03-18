# 스티커, 2024년 3월 18일 18:06:02, 34044kb, 84ms, 566b
# 1초 10만 => nlogn
import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    A=[list(map(int,input().split())) for _ in range(2)]
    dp=[[0]*n for _ in range(2)]
    dp[0][0],dp[1][0]=A[0][0],A[1][0]
    if n>1:
        dp[0][1]=A[1][0]+A[0][1]
        dp[1][1]=A[0][0]+A[1][1]
        for i in range(2,n):
            dp[0][i]=A[0][i]+max(dp[1][i-1],dp[1][i-2])
            dp[1][i]=A[1][i]+max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))