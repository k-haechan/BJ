# 스위치와 램프, 2023년 11월 22일 23:10:46, 31120kb, 48ms, 404b
# 2초, 2000, n^2

import sys
input=sys.stdin.readline

n,m=map(int,input().split())

L=[0]*m
S=[list(map(int,input().split())) for _ in range(n)]
result=0

for s in S:
    for i in range(1,s[0]+1):
        L[s[i]-1]+=1

for s in S:
    check=True
    for i in range(1,s[0]+1):
        if L[s[i]-1] < 2:
            check=False
            break
    if check:
        result=1
        break
print(result)
