# 쉽게 푸는 문제, 2024년 3월 3일 16:27:34, 31756kb, 44ms, 135b
import sys

a, b = map(int, sys.stdin.readline().split())
tmp = []
for i in range(1, 401):
    tmp += [i] * i
print(sum(tmp[a - 1: b]))
