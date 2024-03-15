# 수 정렬하기 2, 2023년 8월 9일 01:11:10, 77108kb, 1324ms, 116b
import sys
input=sys.stdin.readline
n=int(input())
L=sorted(int(input()) for _ in range(n))
for a in L:
    print(a)
