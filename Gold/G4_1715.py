# 카드 정렬하기, 2023년 9월 7일 00:32:25, 37644kb, 552ms, 242b
import sys
from queue import PriorityQueue

input = sys.stdin.readline
n=int(input())
A=PriorityQueue()
for _ in range(n):
    A.put(int(input()))
sum=0
for _ in range(n-1):
    a=A.get()
    b=A.get()
    sum+=(a+b)
    A.put(a+b)
print(sum)
