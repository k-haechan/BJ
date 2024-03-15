# 키로거, 2024년 2월 29일 18:52:21, 44128kb, 940ms, 461b
from collections import deque
n=int(input())


for _ in range(n):
    left=[]
    right=deque()
    s=input()
    for c in s:
        if c=='<':
            if left:
                right.appendleft(left.pop())
        elif c=='>':
            if right:
                left.append(right.popleft())
        elif c=='-':
            if left:
                left.pop()
        else:
            left.append(c)
            
    print(''.join(left)+''.join(right))
