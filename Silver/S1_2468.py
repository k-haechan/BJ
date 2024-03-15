# 안전 영역, 2024년 3월 2일 20:25:23, 34088kb, 756ms, 889b
from collections import deque
def bfs(A,r,c):
    dq=deque()
    dq.append((r,c))
    n=len(A)
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]

    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and A[nx][ny]>0:
                A[nx][ny]=0
                dq.append((nx,ny))
            

def getSafeArea(A):
    n=len(A)
    answer=0
    for i in range(n):
        for j in range(n):
            if A[i][j]>0:
                bfs(A,i,j)
                answer+=1
    return answer

n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
answer=1
for _ in range(1,101):
    for i in range(n):
        for j in range(n):
            A[i][j]-=1
    A_=[A[i][:] for i in range(n)]
    value=getSafeArea(A_)
    if value>answer:
        answer=value
    elif value==0:
        break
print(answer)
