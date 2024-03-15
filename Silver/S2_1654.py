# 랜선 자르기, 2024년 2월 23일 17:19:49, 31120kb, 88ms, 272b
import sys 
input = sys.stdin.readline

k,n=map(int,input().split())
A=sorted(int(input()) for _ in range(k))
s,e=1,A[-1]
while s<=e:
    m=(s+e)//2
    cnt=0
    for a in A:
        cnt+=a//m
    if cnt>=n:# 잘게 쪼개면
        s=m+1
    else:
        e=m-1
print(e)
