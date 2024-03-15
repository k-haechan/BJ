# LCS, 2024년 2월 19일 12:47:49, 31120kb, 528ms, 265b
s1=input()
s2=input()
n1=len(s1)
n2=len(s2)
dp=[0]*(n2+1)
for i in range(n1):
    tmp=dp[:]
    for j in range(n2):
        if s1[i]==s2[j] and dp[j]<i+1:
            dp[j+1]=max(dp[j+1],tmp[j]+1)
        else:
            dp[j+1]=max(dp[j+1],dp[j])

print(dp[n2])

