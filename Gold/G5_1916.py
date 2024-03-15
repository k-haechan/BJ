# 최소비용 구하기, 2023년 9월 19일 00:12:31, 60176kb, 556ms, 655b
#최소비용구하기
from queue import PriorityQueue
import sys
input= sys.stdin.readline
n=int(input())
m=int(input())
A=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    A[s].append((e,w))
start,end=map(int,input().split())

q=PriorityQueue()
q.put((0,start))
visited=[False]*(n+1)
cost=[sys.maxsize]*(n+1)
while not q.empty():
    w_now,now = q.get()
    if visited[now]:
        continue
    else:
        visited[now]=True
        cost[now]=w_now
        for next,w in A[now]:
            if cost[next]>cost[now]+w:
                cost[next]=cost[now]+w
                q.put((cost[next],next))

print(cost[end])
