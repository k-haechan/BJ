# 골드바흐 파티션, 2023년 8월 10일 00:58:26, 43168kb, 3084ms, 428b
# 골드바흐 파티션(소수)
# dp로 소수를 구한 후?
import sys
input = sys.stdin.readline

prime=set()
dp=[0]*1000001
dp[1]=1
for i in range(2,1000001):
    if dp[i]==0:
        prime.add(i)
        for j in range(i,1000001,i):
            dp[j]=1

t=int(input())
for _ in range(t):
    n=int(input())
    cnt=0
    for i in range(2,n//2+1):
        if i in prime and (n-i) in prime:
            cnt+=1
    print(cnt)
