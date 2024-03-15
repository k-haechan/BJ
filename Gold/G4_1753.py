# 최단경로, 2024년 2월 24일 10:27:51, 71692kb, 892ms, 685b
import sys
from queue import PriorityQueue
input=sys.stdin.readline

n,m=map(int,input().split())
k=int(input())
dist=[sys.maxsize]*(n+1)
A=[[]for _ in range(n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    A[u].append((v,w))

pq=PriorityQueue()
pq.put((0,k))
dist[k]=0
while not pq.empty():
    n_dist,now=pq.get()
    if n_dist>dist[now]: # visit역할. 이미 최단 경로로 왔었으면 굳이 안가도 됨
        continue
    for next,w in A[now]:
        if dist[next]>dist[now]+w:
            dist[next]=dist[now]+w
            pq.put((dist[next],next))
for i in range(1,n+1):
    if dist[i]!=sys.maxsize:
        print(dist[i])
    else:
        print("INF")
