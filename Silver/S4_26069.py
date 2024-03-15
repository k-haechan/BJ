# 붙임성 좋은 총총이, 2023년 8월 11일 11:47:33, 31256kb, 40ms, 255b
# 붙임성 좋은 총총이
import sys
input = sys.stdin.readline
n=int(input())
dance = {'ChongChong'}

for i in range(1,n+1):
    a, b = input().split()

    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))
