# 경로 찾기, 2023년 9월 19일 20:10:24, 31256kb, 144ms, 313b
# 경로 찾기
import sys
input=sys.stdin.readline
n=int(input())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if A[i][j]==0:
                A[i][j]=A[i][k] and A[k][j]

for i in range(n):
    print(*A[i])
