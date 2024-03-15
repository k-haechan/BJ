# 좌표 정렬하기 2, 2023년 8월 9일 15:12:06, 59988kb, 336ms, 215b
import sys
input = sys.stdin.readline

n=int(input())
points=[]
for _ in range(n):
    points.append(list(map(int,input().split())))
for point in sorted(points,key=lambda x:(x[1],x[0])):
    print(point[0],point[1])
