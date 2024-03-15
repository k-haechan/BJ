# queuestack, 2023년 8월 11일 10:39:56, 47108kb, 188ms, 327b
# queuestack
import sys
input = sys.stdin.readline

n=int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

m=int(input())
C=list(map(int,input().split()))
answer=[]
for i1 in range(n-1,-1,-1):
    if A[i1]==0:
        answer.append(B[i1])
answer+=C
for i in range(m):
    print(answer[i],end=' ')
