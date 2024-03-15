# 물통, 2023년 9월 14일 02:07:14, 34184kb, 64ms, 792b
from collections import deque

limit=list(map(int,input().split()))
visited=[[False]*(limit[1]+1) for _ in range(limit[0]+1)]
answer=[False]*(limit[2]+1)
move=((0,1),(0,2),(1,0),(1,2),(2,0),(2,1))
dq=deque()
dq.append((0,0))
visited[0][0]=True
answer[limit[2]]=True
while dq:
    a,b=dq.popleft()
    c=limit[2]-(a+b)
    now=(a,b,c)
    for x,y in move: #x->y(index)
        next=list(now)
        next[y]+=next[x]
        next[x]=0
        if next[y]>limit[y]:
            next[x]=next[y]-limit[y] 
            next[y]=limit[y]
        if not visited[next[0]][next[1]]:
            visited[next[0]][next[1]]=True
            dq.append((next[0],next[1]))
            if next[0]==0:
                answer[next[2]]=True

for i in range(limit[2]+1):
    if answer[i]:
        print(i,end=' ')

