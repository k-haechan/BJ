# 타임머신, 2023년 9월 19일 18:10:03, 32276kb, 932ms, 696b
import sys
input=sys.stdin.readline
INF=sys.maxsize

n,m=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(m)]
distance=[INF]*(n+1)
distance[1]=0

for i in range(n-1):
    for start,end,time in edges:
        if distance[start]!=INF:
            if distance[end]>distance[start]+time:
                distance[end]=distance[start]+time

cycle=False
for start,end,time in edges:
        if distance[start]!=INF:
            if distance[end]>distance[start]+time:
                cycle=True
                break
if not cycle:
    for i in range(2,n+1):
        if distance[i]!=INF:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)
