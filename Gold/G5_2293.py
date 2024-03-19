# 물통, 2024년 3월 19일 23:54:35, 31120kb, 212ms, 205b
import sys
input = sys.stdin.readline

n,k=map(int,input().split())
A=sorted(int(input()) for _ in range(n))
dp=[0]*(k+1)
dp[0]=1
for a in A:
    for i in range(a,k+1):
        dp[i]+=dp[i-a]
print(dp[-1])