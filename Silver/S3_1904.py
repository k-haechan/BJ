# 01타일, 2024년 2월 18일 18:12:37, 69652kb, 364ms, 117b
dp=[0]*1000001
dp[0]=dp[1]=1
for i in range(2,1000001):
    dp[i]=(dp[i-1]+dp[i-2])%15746
n=int(input())
print(dp[n])
