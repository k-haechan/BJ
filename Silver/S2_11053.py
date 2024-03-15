# 가장 긴 증가하는 부분 수열, 2024년 2월 19일 03:21:37, 31120kb, 156ms, 229b
# 가장 긴 증가하는 부분 수열
N=int(input())
array=list(map(int,input().split()))
dp = [1]*N
for i in range(1,N):
    for j in range(i):
        if array[i]>array[j]: 
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
