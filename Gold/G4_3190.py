# 뱀, 2024년 3월 6일 14:41:50, 34104kb, 72ms, 800b
from collections import deque

n=int(input())
board=[[0]*(n+1) for _ in range(n+1)]
board[1][1]=2
snake=deque()
snake.append((1,1))
route=[]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
d=3

k=int(input())
for _ in range(k):
    r,c=map(int,input().split())
    board[r][c]=1

l=int(input())

for _ in range(l):
    x,c=input().split()
    route.append((int(x),c))

idx=0
sec=0
while True:
    head=snake[-1]
    sec+=1
    nx=head[0]+dx[d]
    ny=head[1]+dy[d]
    if nx<1 or nx>n or ny<1 or ny>n or board[nx][ny]==2:
        print(sec)
        break
    if board[nx][ny]==0:
        x_,y_=snake.popleft()
        board[x_][y_]=0
    snake.append((nx,ny))
    board[nx][ny]=2
    if idx<l and sec==route[idx][0]:
        if route[idx][1]=='L':
            d=(d+1)%4
        else:
            d=(d+3)%4
        idx+=1
