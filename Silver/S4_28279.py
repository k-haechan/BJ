# 덱 2, 2023년 8월 11일 00:31:56, 70652kb, 1484ms, 556b
# 덱 2
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
dq=deque()

for _ in range(n):
    x=list(map(int,input().split()))

    if x[0]==1:
        dq.appendleft(x[1])
    elif x[0]==2:
        dq.append(x[1])
    elif x[0]==3:
        print(dq.popleft() if dq else -1)
    elif x[0]==4:
        print(dq.pop() if dq else -1)
    elif x[0]==5:
        print(len(dq))
    elif x[0]==6:
        print(0 if dq else 1)
    elif x[0]==7:
        print(dq[0] if dq else -1)
    elif x[0]==8:
        print(dq[-1] if dq else -1)
