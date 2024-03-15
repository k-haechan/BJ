# 가장 긴 바이토닉 부분 수열, 2024년 2월 19일 03:40:02, 31120kb, 300ms, 373b
n=int(input())
A=list(map(int,input().split()))
dp1=[1]*n
dp2=[1]*n
for i in range(1,n):
    for j in range(i):
        if A[i]>A[j]: # 증가
            if dp1[j]+1>dp1[i]:
                dp1[i]=dp1[j]+1
        if A[n-1-i]>A[n-1-j]: # 감소
            if dp2[n-1-j]+1>dp2[n-1-i]:
                dp2[n-1-i]=dp2[n-1-j]+1
print(max([dp1[i]+dp2[i]-1 for i in range(n)]))
