# 최소 힙, 2024년 2월 23일 22:07:18, 37044kb, 120ms, 224b
import sys,heapq
input=sys.stdin.readline

min_heap=[]
n=int(input())

for _ in range(n):
    x=int(input())
    if x==0:
        print(heapq.heappop(min_heap) if min_heap else 0)
    else:
        heapq.heappush(min_heap,x)
