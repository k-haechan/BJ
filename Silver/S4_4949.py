# 균형잡힌 세상, 2023년 8월 10일 12:52:54, 31256kb, 80ms, 456b
# 균형잡힌 세상

import sys
input = sys.stdin.readline

open=['(','[']
close=[')',']']
answer=dict(zip(close,open))
while True:
    s=input().rstrip('\n')
    stack=[]
    tag=True
    if s=='.': break
    for c in s:
        if c in open:
            stack.append(c)
        elif c in close:
            if not stack or answer[c]!=stack.pop():
                tag=False
                break
    if stack: tag=False
    print('yes' if tag else 'no')
