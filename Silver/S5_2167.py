# 2차원 배열의 합, 2024년 3월 5일 04:54:52, 37032kb, 120ms, 511b
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(n)]
sumArr=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        sumArr[i][j]=sumArr[i][j-1]+arr[i-1][j-1]
for i in range(2,n+1):
    for j in range(1,m+1):
        sumArr[i][j]=sumArr[i-1][j]+sumArr[i][j]



k=int(input())
for _ in range(k):
    i,j,x,y=map(int,input().split())
    print(sumArr[x][y]+sumArr[i-1][j-1]-sumArr[x][j-1]-sumArr[i-1][y])
