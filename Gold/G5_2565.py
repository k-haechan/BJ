# 전깃줄, 2024년 2월 19일 11:32:30, 31120kb, 56ms, 231b
n=int(input())
A=sorted(list(map(int,input().split())) for _ in range(n))
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if A[i][1]>A[j][1]:
            if dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
print(n-max(dp))
