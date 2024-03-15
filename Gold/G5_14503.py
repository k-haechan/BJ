# 로봇 청소기, 2024년 3월 5일 14:45:34, 31196kb, 44ms, 711b
import sys
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m=map(int,input().split())
r,c,d=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(n)]
answer=0
def dfs(r,c,d):
    global answer
    if room[r][c]==0: 
        room[r][c]=2
        answer+=1
    
    isFull=True
    for _ in range(4): # 반시계방향 탐색
        d=(d+3)%4 # 반시계 방향
        x=r+dx[d]
        y=c+dy[d]
        if room[x][y]==0: # 청소되지 않은 빈칸이 있는 경우
            dfs(x,y,d)
            isFull=False
    if isFull:
        x=r-dx[d]
        y=c-dy[d]
        if room[x][y]==1:
            print(answer)
            sys.exit()
            return
        dfs(x,y,d)

dfs(r,c,d)
print(answer)
