# K번째 최단경로 찾기, 2023년 9월 19일 10:20:43, 66700kb, 4096ms, 682b
import sys
from queue import PriorityQueue
input=sys.stdin.readline

n,m,k=map(int,input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,input().split())
    A[s].append((e,w))
distance=[[sys.maxsize]*(k) for _ in range(n+1)]

q=PriorityQueue()
q.put((0,1))
distance[1][0]=0

while not q.empty():
    costNow,now=q.get()
    for next,costNext in A[now]:
        cost=costNow+costNext
        if distance[next][k-1]>cost:
            distance[next][k-1]=cost
            distance[next].sort()
            q.put((cost,next))
           
for i in range(1,n+1):
    if distance[i][k-1]==sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])
