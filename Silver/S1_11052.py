# 카드 구매하기, 2024년 3월 18일 18:49:25, 31252kb, 104ms, 217b
# 1000, 1초, n^2
n=int(input())
A=list(map(int,input().split()))
dp=[0]*n
dp[0]=A[0]
for i in range(1,n):
    m=(i+1)//2
    B=[0]*(m+1)
    for j in range(m):
        B[j]=dp[j]+dp[i-j-1]
    B[m]=A[i]
    dp[i]=max(B)
print(dp[n-1])
