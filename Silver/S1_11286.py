# 절댓값 힙, 2023년 9월 4일 20:50:03, 44036kb, 296ms, 434b
# 절대값 힙 구현하기
from queue import PriorityQueue
import sys
input = sys.stdin.readline
n=int(input())
pq=PriorityQueue()

for _ in range(n):
    request=int(input())
    if request == 0:
        if pq.empty():
            print('0')
        else:
            tmp=pq.get() # 가장 앞에 있는 값을 추출
            print(str(tmp[1]))
    else:
        pq.put((abs(request),request)) # 우선순위 큐에 값 넣기

