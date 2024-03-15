# 연구소, 2024년 3월 2일 02:12:50, 34104kb, 1688ms, 1093b
from itertools import combinations
from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
virus=[]
# 0인 부분 구하기
zero_space=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            zero_space.append((i,j))
        if board[i][j]==2:
            virus.append((i,j))

# 바이러스 확장 함수 만들기
def bfs(virus,board,cnt):
    dq=deque()
    for x,y in virus:
        dq.append((x,y))
    dx=(-1,0,1,0)
    dy=(0,-1,0,1)
    
    while dq:
        x_,y_=dq.popleft()
        for i in range(4):
            nx=x_+dx[i]
            ny=y_+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==0:
                    dq.append((nx,ny))
                    board[nx][ny]=2
                    cnt-=1
    return cnt


# 3곳을 고르기
zero2one=combinations(zero_space,3)

max_=-float('inf')
for walls in zero2one:
    board_=[board[i][:] for i in range(n)]
    for x,y in walls:
        board_[x][y]=1
    max_=max(max_,bfs(virus,board_,len(zero_space)-3))
print(max_)
