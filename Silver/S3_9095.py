# 1, 2, 3 더하기, 2023년 7월 31일 22:06:58, 31256kb, 40ms, 237b
# 1, 2, 3 더하기

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a=int(input())     
    dp=[0]*12
    dp[1], dp[2], dp[3] = 1,2,4
    for i in range(4,12):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[a])
