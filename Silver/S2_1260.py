# DFS와 BFS, 2024년 2월 24일 01:11:20, 36932kb, 100ms, 759b
import sys
from queue import deque
input=sys.stdin.readline

n,m,v = map(int,input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    A[a].append(b)
    A[b].append(a)
for i in range(1,n+1):
    A[i].sort()

def dfs():
    for j in A[arr[-1]]:
        if not visited[j]:
            visited[j]=True
            arr.append(j)
            dfs()
            
visited=[False]*(n+1)
arr=[v]
visited[v]=True
dfs()
print(*arr)

def bfs():
    dq=deque()
    dq.append(v)
    visited=[False]*(n+1)
    visited[v]=True
    arr=[]
    while dq:
        f=dq.popleft()
        arr.append(f)
        for t in A[f]:
            if not visited[t]:
                dq.append(t)
                visited[t]=True
    print(*arr)
bfs()
