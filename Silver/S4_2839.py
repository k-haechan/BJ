# 설탕 배달, 2023년 7월 31일 19:48:04, 31256kb, 48ms, 273b
# 설탕 배달

'''
- 문제풀이 방법:
3 6 9 12 ...
5 10 15 20
8, 11, 13 ..
- dp[3] = 1
- dp[4] = -1
- dp[18] = dp[15]
'''
N = int(input())
answer=0
while N>0:
    if N%5 == 0:
        answer+=(N//5)
        break
    answer+=1
    N-=3
print(answer if N>=0 else -1)


