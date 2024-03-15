# 최대 힙, 2024년 2월 23일 22:03:39, 37044kb, 120ms, 209b
import sys,heapq
input=sys.stdin.readline

n=int(input())
heap=[]
for _ in range(n):
    x=int(input())
    if x==0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap,-x)
