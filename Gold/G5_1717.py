# 집합의 표현, 2024년 2월 24일 12:11:02, 70676kb, 292ms, 553b
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
parent=list(range(n+1))

def find(a):
    if a!=parent[a]:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
def checkSame(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    else:
        return 0


for _ in range(m):
    x,a,b=map(int,input().split())
    if x==1:
        if checkSame(a,b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)

