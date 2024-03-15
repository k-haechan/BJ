# 색종이 올려 놓기, 2024년 3월 1일 20:16:31, 31120kb, 44ms, 375b
import sys
input=sys.stdin.readline

n=int(input())
A=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a==b:
        A.append((a,b))
    else:
        A.append((a,b))
        A.append((b,a))
A.sort()
dp=[1]*len(A)
for i in range(len(A)):
    for j in range(i):
        if A[i][0]>=A[j][0] and A[i][1]>=A[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
