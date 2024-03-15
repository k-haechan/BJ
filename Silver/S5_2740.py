# 행렬 곱셈, 2023년 9월 2일 19:05:01, 31256kb, 168ms, 432b
# 행렬 곱셈
import sys
input = sys.stdin.readline

n,m=map(int,input().rstrip().split())
A=[list(map(int,input().rstrip().split())) for _ in range(n)]

m,k=map(int,input().rstrip().split())
B=[list(map(int,input().rstrip().split())) for _ in range(m)]
C=[[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            C[i][j]+=A[i][l]*B[l][j]
        print(C[i][j],end=' ')
    print()
