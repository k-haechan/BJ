# 구간 합 구하기 4, 2023년 8월 23일 22:43:07, 41316kb, 276ms, 329b
import sys 
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

sumArr=[0]*n
sumArr[0]=arr[0]
for i in range(1,n):
    sumArr[i]=arr[i]+sumArr[i-1]

for _ in range(m):
    i,j=map(int,input().split())
    if i>1:
        print(sumArr[j-1]-sumArr[i-2])
    else:
        print(sumArr[j-1])
