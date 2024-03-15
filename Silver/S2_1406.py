# 에디터, 2024년 2월 29일 03:07:39, 38992kb, 264ms, 401b
import sys
from collections import deque

input=sys.stdin.readline

L=list(input().rstrip())
R=deque()
n=int(input())

for _ in range(n):
    order=input().rstrip()
    if order=='L' and L:
        R.appendleft(L.pop())
    elif order=='D' and R:
        L.append(R.popleft())
    elif order=='B' and L:
        L.pop()
    elif order[0]=='P':
        L.append(order[-1])

print(''.join(L)+''.join(R))
