# 좌표 정렬하기, 2023년 8월 9일 15:09:15, 51644kb, 372ms, 190b
import sys
input = sys.stdin.readline

n=int(input())
points=[]
for _ in range(n):
    points.append(list(map(int,input().split())))
for point in sorted(points):
    print(point[0],point[1])
