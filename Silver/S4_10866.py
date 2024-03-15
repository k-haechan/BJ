# 덱, 2024년 2월 29일 14:16:49, 34036kb, 72ms, 644b
import sys
from collections import deque
input = sys.stdin.readline

Deque=deque()
n=int(input())
for _ in range(n):
    a=input().rstrip().split()
    if a[0]=='push_back':
        Deque.append(a[1])
    elif a[0]=='push_front':
        Deque.appendleft(a[1])
    elif a[0]=='pop_front':
        print(Deque.popleft() if Deque else -1)
    elif a[0]=='pop_back':
        print(Deque.pop() if Deque else -1)
    elif a[0]=='size':
        print(len(Deque))
    elif a[0]=='empty':
        print(0 if Deque else 1)
    elif a[0]=='front':
        print(Deque[0] if Deque else -1)
    else: #a[0]=='back'
        print(Deque[-1] if Deque else -1)
