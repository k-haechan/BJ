# 덩치, 2024년 3월 2일 19:41:30, 31120kb, 40ms, 280b
import sys
input=sys.stdin.readline

n=int(input())
A=list(list(map(int,input().split())) for _ in range(n))
answer=[0]*n
for i in range(n):
    order=1
    for j in range(n):
        if A[i][0]<A[j][0] and A[i][1]<A[j][1]:
            order+=1
    answer[i]=order
print(*answer)

