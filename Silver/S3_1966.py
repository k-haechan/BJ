# 프린터 큐, 2024년 3월 3일 14:28:08, 34052kb, 68ms, 516b
import sys
input=sys.stdin.readline
from collections import deque
T=int(input())
for _ in range(T):
    n,m=map(int,input().rstrip().split())
    dq=deque(map(int,input().rstrip().split()))
    target=dq[m]
    cnt=0
    while True:
        if dq[0]==max(dq):
            dq.popleft()
            cnt+=1
            m-=1
            if m<0:
                print(cnt)
                break
            
        else:
            dq.append(dq.popleft())
            m-=1
            if m<0:
                m+=len(dq)
