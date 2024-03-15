# 나머지 합, 2024년 2월 18일 16:17:19, 153764kb, 596ms, 250b
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
A=list(map(int,input().split()))
B=[0]*m
s=A[0]
B[s%m]+=1
for i in range(1,len(A)):
    s+=A[i]
    B[s%m]+=1
B[0]+=1
answer=0
for x in B:
    answer+=x**2-x
answer//=2
print(answer)
