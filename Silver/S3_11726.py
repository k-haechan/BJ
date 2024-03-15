# 2×n 타일링, 2023년 8월 1일 02:53:25, 31256kb, 48ms, 182b
import sys
input = sys.stdin.readline

n=int(input())

dp = [0]*(1001)
dp[1]=1
dp[2]=2
if n>=3:
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
#print(dp)
print(dp[n]%10007)
