# 구간 합 구하기 5, 2023년 8월 25일 12:33:11, 72508kb, 1100ms, 750b
# 구간 합 구하기 5
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

prefixSum=[[0]*(n) for _ in range(n)]
l=list(map(int,input().split()))
prefixSum[0][0]=l[0]
for i in range(1,n):
    prefixSum[0][i]+=prefixSum[0][i-1]+l[i]

for i in range(1,n):
    l=list(map(int,input().split()))
    prefixSum[i][0]=l[0]
    for j in range(1,n):
        prefixSum[i][j]=prefixSum[i][j-1]+l[j]
    for j in range(n):
        prefixSum[i][j]+=prefixSum[i-1][j]

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    answer=prefixSum[x2-1][y2-1]
    if y1!=1:
        answer-=prefixSum[x2-1][y1-2]
    if x1!=1:
        answer-=prefixSum[x1-2][y2-1]
    if x1!=1 and y1!=1:
        answer+=prefixSum[x1-2][y1-2]
    print(answer)
