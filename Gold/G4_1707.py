# 이분 그래프, 2023년 9월 16일 15:06:49, 52000kb, 1252ms, 803b
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    dq=deque()
    state[v]=0
    dq.append((A[v],state[v]))
  
    while dq:
        x,s=dq.pop()
        for y in x:
            if state[y]==-1:
                state[y]=not s
                dq.append((A[y],state[y]))
            else:
                if state[y]==s:
                    return False
    return True

n=int(input())
for _ in range(n):
    n,e=map(int,input().split())
    A=[[] for _ in range(n+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        A[a].append(b)
        A[b].append(a)

    state=[-1]*(n+1)

    ans=True
    for i in range(1,n+1):
        if state[i]==-1:
            if not bfs(i):
                ans=False
                break
    print('YES' if ans else 'NO')
