# 여행 가자, 2024년 2월 24일 12:50:51, 31120kb, 48ms, 486b
import sys
input=sys.stdin.readline

n,m=int(input()),int(input())
parent=list(range(n))

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

for i in range(n):
    A=list(map(int,input().split()))
    for j in range(n):
        if A[j]==1:
            union(i,j)
B=list(map(int,input().split()))
if len({find(b-1) for b in B})==1:
    print('YES')
else:
    print('NO')
