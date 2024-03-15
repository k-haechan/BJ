# 최솟값 찾기, 2023년 9월 4일 15:20:07, 756308kb, 7640ms, 271b
from collections import deque
n,l=map(int,input().split())
A=list(map(int,input().split()))
dq=deque()

for i in range(n):
    while dq and dq[-1][0]>=A[i]:
        dq.pop()
    dq.append((A[i],i))

    if dq[0][1]<=i-l:
        dq.popleft()

    print(dq[0][0], end=' ')
