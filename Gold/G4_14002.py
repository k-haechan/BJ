# 가장 긴 증가하는 부분 수열 4, 2024년 2월 26일 15:50:23, 31120kb, 120ms, 394b
import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
dp=[[1,[A[i]]] for i in range(n)]
answer=dp[0]
for i in range(1,n):
    for j in range(i):
        if A[i]>A[j]:
            if dp[i][0]<dp[j][0]+1:
                dp[i][0]=dp[j][0]+1
                dp[i][1]=dp[j][1]+[A[i]]
    if dp[i][0]>answer[0]:
        answer=dp[i]

print(answer[0])
print(*answer[1])
