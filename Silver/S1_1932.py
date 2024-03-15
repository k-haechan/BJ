# 정수 삼각형, 2024년 2월 18일 18:59:49, 31120kb, 136ms, 188b
n=int(input())
dp=[int(input())]
for i in range(2,n+1):
    A=list(map(int,input().split()))
    A[0]+=dp[0]
    for j in range(1,i):
        A[j]+=max(dp[j-1:j+1])
    dp=A
print(max(dp))
