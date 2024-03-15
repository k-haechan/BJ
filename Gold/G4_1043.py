# 거짓말, 2023년 9월 16일 21:36:45, 31256kb, 48ms, 652b
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
true=list(map(int,input().split()))[1:]
party=[list(map(int,input().split())) for _ in range(m)]
parent=list(range(n+1))

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b): # 첫번째 사람이 대표
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

for i in range(m):
    for j in range(1,party[i][0]):
        union(party[i][j],party[i][j+1])

answer=m
for i in range(m):
    for t in true:
        if find(party[i][1])==find(t):
            answer-=1
            break
print(answer)

