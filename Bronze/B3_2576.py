# 홀수, 2024년 2월 28일 11:40:17, 33188kb, 44ms, 159b
import heapq

A=[]
for _ in range(7):
    n=int(input())
    if n%2==1:
        heapq.heappush(A,n)
if A:
    print(sum(A))
    print(A[0])
else:
    print(-1)
