# 공유기 설치, 2024년 2월 23일 19:26:41, 38848kb, 400ms, 591b
import sys
input = sys.stdin.readline

n,c=map(int,input().split())
A=sorted(int(input()) for _ in range(n))
s,e=1,A[-1]-A[0] # 가장 인접한 거리는 1~A[-1]-A[0]
                 # 이분탐색으로 가장 인접한 거리의 '최댓값' 구하기
while s<=e:
    m=(s+e)//2
    cnt=1
    a_=A[0]
    for a in A:  # 가장 인접한 거리가 m일 때 조건을 만족하는지
        if a-a_>=m:
            cnt+=1 # greedy count
            a_=a   # 이전 집의 위치
    if cnt>=c:     # 최댓값이기 때문에 여기에 등호
        s=m+1
    else:
        e=m-1
print(e)
