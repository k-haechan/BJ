# 게임 개발, 2023년 9월 17일 12:33:31, 34160kb, 96ms, 621b
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
time=[0]*(n+1)
answer=[0]*(n+1)
degree=[0]*(n+1)
A=[[] for _ in range(n+1)]
for i in range(1,n+1):
    L=list(map(int,input().split()))
    time[i]=L[0]
    for j in range(1,len(L)-1):
        A[L[j]].append(i)
        degree[i]+=1

dq=deque()
for i in range(1,n+1):
    if degree[i]==0:
        dq.append(i)

while dq:
    x=dq.popleft()
    answer[x]+=time[x]
    for i in A[x]:
        degree[i]-=1
        answer[i]=max(answer[i],answer[x])
        if degree[i]==0:
            dq.append(i)

for i in range(1,n+1):
    print(answer[i])
