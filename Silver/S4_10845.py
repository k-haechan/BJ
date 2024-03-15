# 큐, 2024년 2월 29일 14:08:22, 34160kb, 76ms, 481b
import sys
from collections import deque
input = sys.stdin.readline

queue=deque()
n=int(input())
for _ in range(n):
    a=input().rstrip()
    if a[:3]=='pus':
        queue.append(a.split()[-1])
    elif a[:3]=='pop':
        print(queue.popleft() if queue else -1)
    elif a=='size':
        print(len(queue))
    elif a=='empty':
        print(0 if queue else 1)
    elif a=='front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
