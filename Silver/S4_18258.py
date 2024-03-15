# 큐 2, 2023년 8월 10일 13:04:01, 175180kb, 1688ms, 514b
# 큐 2

import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
queue=deque()
for _ in range(n):
    s=input().rstrip().split()
    if s[0]=='push':
        queue.append(s[1])   
    elif s[0]=='pop':
        print(queue.popleft() if queue else -1)
    elif s[0]=='front':
        print(queue[0] if queue else -1)
    elif s[0]=='back':
        print(queue[-1] if queue else -1)
    elif s[0]=='size':
        print(len(queue))
    elif s[0]=='empty':
        print(0 if queue else 1)

