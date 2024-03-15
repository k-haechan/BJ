# 임계경로, 2023년 9월 18일 16:43:10, 52924kb, 272ms, 906b
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
A=[[] for _ in range(n+1)]
B=[[] for _ in range(n+1)] # back load\
indegree=[0]*(n+1)
for _ in range(m):
    s,e,w=map(int,input().split())
    A[s].append((e,w))
    B[e].append((s,w))
    indegree[e]+=1

start,end=map(int,input().split())

dq=deque()
dq.append(start)
# 임계경로 구하기
crit_path=[0]*(n+1)

while dq:
    now=dq.popleft()
    for next,w in A[now]:
        crit_path[next]=max(crit_path[next],crit_path[now]+w)
        indegree[next]-=1
        if indegree[next]==0:
            dq.append(next)

check=[False]*(n+1)
cnt=0
dq.append(end)
while dq:
    now=dq.popleft()
    if check[now]==False:
        check[now]=True
        for next,w in B[now]:
            if crit_path[now]-crit_path[next]==w:
                dq.append(next)
                cnt+=1
print(crit_path[end])
print(cnt)
