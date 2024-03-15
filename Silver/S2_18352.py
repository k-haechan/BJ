# 특정 거리의 도시 찾기, 2023년 9월 12일 23:43:34, 105984kb, 1836ms, 617b
import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x=map(int,input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    A[a].append(b)

dq=deque()
visited=[False]*(n+1)

def bfs(v,k):
    ans=[]
    visited[v]=True
    dq.append((v,0))
    while dq:
        x=dq.popleft()
        if x[1]==k:
            ans.append(x[0])
        for i in A[x[0]]:
            if not visited[i]:
                visited[i]=True
                dq.append((i,x[1]+1))
    if not ans:
        print(-1)
    else:
        for a in sorted(ans):
            print(a)
bfs(x,k)
