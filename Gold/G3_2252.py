# 줄 세우기, 2023년 9월 17일 00:32:08, 38936kb, 4116ms, 449b
# 줄세우기
from collections import deque
n,m=map(int,input().split())
degree=[0]*(n+1)
A=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    A[s].append(e)
    degree[e]+=1

dq=deque()
for i in range(1,n+1):
    if degree[i]==0:
        dq.append(i)

answer=[]
while dq:
    x=dq.popleft()
    answer.append(x)
    for i in A[x]:
        degree[i]-=1
        if degree[i]==0:
            dq.append(i)

print(*answer)
