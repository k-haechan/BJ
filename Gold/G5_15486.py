# 퇴사 2, 2023년 11월 23일 02:18:05, 252216kb, 2908ms, 330b
# NlogN
import sys
input=sys.stdin.readline

n=int(input())
A=[tuple(map(int,input().split())) for _ in range(n)]
dp=[0]*n
if A[0][0]-1<n:
    dp[A[0][0]-1]=max(dp[A[0][0]-1],A[0][1])
for i in range(1,n):
    if i+A[i][0]-1<n:
        dp[i+A[i][0]-1]=max(dp[i+A[i][0]-1],dp[i-1]+A[i][1])
    dp[i]=max(dp[i-1],dp[i])
print(dp[-1])
