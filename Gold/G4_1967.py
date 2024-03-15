# 트리의 지름, 2023년 9월 6일 21:30:24, 34520kb, 92ms, 667b
import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
A=[[] for _ in range(n+1)]
width=[0]*(n+1)
for _ in range(n-1):
    tmp=list(map(int,input().rstrip().split()))
    A[tmp[0]].append((tmp[1],tmp[2]))
    A[tmp[1]].append((tmp[0],tmp[2]))

for i in range(1,n+1):
    A[i].sort()

def bfs(v):
    visited=[False]*(n+1)
    visited[v]=True
    dq=deque()
    res=[v,0]
    dq.append(res)
    while dq:
        x,w1=dq.popleft()
        if w1>res[1]:
            res=x,w1
        for i,w2 in A[x]:
            if not visited[i]:
                dq.append((i,w1+w2))
                visited[i]=True
    return res
print(bfs(bfs(1)[0])[1])
