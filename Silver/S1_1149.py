# RGB거리, 2024년 2월 18일 18:51:43, 31120kb, 44ms, 246b
import sys
input = sys.stdin.readline

n=int(input())
dp=list(map(int,input().split()))

for _ in range(n-1):
    A=list(map(int,input().split()))
    for i in range(3):
        A[i]+=min([dp[j] for j in range(3) if i!=j])
    dp=A
print(min(dp))
