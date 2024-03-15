# Strfry, 2024년 2월 29일 03:13:33, 31120kb, 148ms, 196b
import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    a,b=input().rstrip().split()
    if sorted(a)==sorted(b):
        print('Possible')
    else:
        print('Impossible')
