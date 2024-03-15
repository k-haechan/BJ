# 분산처리, 2024년 3월 3일 16:01:25, 31120kb, 40ms, 279b
import sys
input=sys.stdin.readline
n=int(input())
A=[[i] for i in range(10)]
A[0][0]=10
for i in range(2,10):
    while (A[i][-1]*i)%10!=i:
        A[i].append((A[i][-1]*i)%10)
for _ in range(n):
    a,b=map(int,input().split())
    a%=10
    b-=1
    print(A[a][(b)%len(A[a])])
