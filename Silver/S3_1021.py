# 회전하는 큐, 2024년 2월 29일 18:24:28, 34016kb, 64ms, 263b
from collections import deque

n,m=map(int,input().split())
dq=deque(range(1,n+1))
A=list(map(int,input().split()))
answer=0

for a in A:
    idx=dq.index(a)
    r_idx=len(dq)-idx
    dq.rotate(r_idx)
    dq.popleft()
    answer+=min(idx,r_idx)
    
print(answer)
