# 미로 탐색, 2024년 2월 24일 02:01:48, 34044kb, 84ms, 566b
import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
A=[input() for _ in range(n)]
visited=[[False]*m for _ in range(n)]
visited[0][0]=True
dq=deque()
dq.append((0,0,1))

direction=[(0,1),(0,-1),(-1,0),(1,0)]

while dq:
    r,c,move=dq.popleft()
    if r==n-1 and c==m-1:
        print(move)
        break
    for r_,c_ in direction:
        _r,_c=r+r_,c+c_
        if 0<=_r<n and 0<=_c<m:
            if not visited[_r][_c] and A[_r][_c]!='0':
                dq.append((_r,_c,move+1))
                visited[_r][_c]=True
