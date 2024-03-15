# 케빈 베이컨의 6단계 법칙, 2023년 9월 21일 02:30:27, 31120kb, 312ms, 578b
# 케빈 베이커. -> 40000 40KB~
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=[[sys.maxsize if i!=j else 0 for j in range(n+1)] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    A[a][b]=1
    A[b][a]=1

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if A[s][k]!=sys.maxsize and A[k][e]!=sys.maxsize:
                A[s][e]=min(A[s][e],A[s][k]+A[k][e])

s=sys.maxsize
result=-1
for i in range(1,n+1):
    tmp=sum(A[i][1:])
    if tmp<s:
        s=tmp
        result=i
print(result)
