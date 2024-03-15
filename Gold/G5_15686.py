# 치킨 배달, 2024년 3월 2일 04:03:31, 31120kb, 604ms, 644b
import sys
from itertools import combinations
input = sys.stdin.readline

n,m=map(int,input().split())
A=[list(map(int,input().rstrip().split())) for _ in range(n)]
chicken=[]
home=[]

for i in range(n):
    for j in range(n):
        if A[i][j]==1:
            home.append((i,j))
        elif A[i][j]==2:
            chicken.append((i,j))
min_city_dist=float('inf')
for chick in combinations(chicken,m):
    city_dist=0
    for h in home:
        dist=float('inf')
        for chi in chick:
            dist=min(dist,abs(h[0]-chi[0])+abs(h[1]-chi[1]))
        city_dist+=dist
    min_city_dist=min(city_dist,min_city_dist)
print(min_city_dist)
