# 바이러스, 2024년 2월 24일 02:13:27, 34036kb, 68ms, 452b
import sys
from collections import deque

n,m=int(input()),int(input())
A=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    A[a].append(b)
    A[b].append(a)

dq=deque()
dq.append(1)
visited=[False]*(n+1)
visited[1]=True
cnt=0
while dq:
    from_ = dq.popleft()
    for to in A[from_]:
        if not visited[to]:
            visited[to]=True
            dq.append(to)
            cnt+=1
print(cnt)
