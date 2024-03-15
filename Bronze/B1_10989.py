# 수 정렬하기 3, 2023년 8월 9일 14:57:32, 31256kb, 8908ms, 187b
import sys
input = sys.stdin.readline
n=int(input())
array=[0]*10001
for _ in range(n):
    array[int(input())]+=1
for i in range(1,10001):
    for _ in range(array[i]):
        print(i)

