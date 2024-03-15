# 카드2, 2023년 8월 10일 13:11:06, 50988kb, 148ms, 179b
import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
deq=deque(range(1,n+1))
for _ in range(n-1):
    deq.popleft()
    deq.rotate(-1)
print(deq[0])
