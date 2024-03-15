# 테트로미노, 2024년 2월 28일 01:05:57, 39028kb, 5472ms, 1188b
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited=[[False]*m for _ in range(n)]
max_=-sys.maxsize

def dfs(x,y,depth=0,sum=0):
    global max_
    visited[x][y]=True
    sum+=A[x][y]
    if depth==3:
        max_=max(max_,sum)
        visited[x][y]=False
        return
    for i in range(4):
        x_=x+dx[i]
        y_=y+dy[i]
        if 0<=x_<n and 0<=y_<m and not visited[x_][y_]:
            dfs(x_,y_,depth+1,sum)
    visited[x][y]=False

def dfs2(x,y):
    global max_
    arr=[]
    for i in range(4):
        x_=x+dx[i]
        y_=y+dy[i]
        if 0<=x_<n and 0<=y_<m:
            arr.append((x_,y_))
    if len(arr)==4:
        arr=arr*2
        for i in range(4):
            tmp=A[x][y]+A[arr[i][0]][arr[i][1]]+A[arr[i+1][0]][arr[i+1][1]]+A[arr[i+2][0]][arr[i+2][1]]
            if tmp>max_:
                max_=tmp
    elif len(arr)==3:
        tmp=A[x][y]+A[arr[0][0]][arr[0][1]]+A[arr[1][0]][arr[1][1]]+A[arr[2][0]][arr[2][1]]
        if tmp>max_:
                max_=tmp

for i in range(n):
    for j in range(m):
        dfs(i,j)
        dfs2(i,j)

print(max_)
