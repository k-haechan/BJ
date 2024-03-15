# 피보나치 수 2, 2023년 8월 4일 12:05:25, 31256kb, 44ms, 94b
dp=[0]*91
dp[1]=1
for i in range(2,91):
    dp[i]=dp[i-2]+dp[i-1]

n=int(input())
print(dp[n])
