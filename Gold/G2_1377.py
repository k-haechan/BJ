# 버블 소트, 2023년 9월 4일 21:12:46, 120908kb, 1008ms, 150b
import sys
input = sys.stdin.readline

n=int(input())
l=sorted((int(input()),i) for i in range(n))
arr=[l[i][1]-i for i in range(n)]
print(max(arr)+1)
