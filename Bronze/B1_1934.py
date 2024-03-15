# 최소공배수, 2023년 9월 11일 23:03:29, 31256kb, 56ms, 175b
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    lcm=a*b
    while a!=0:
        a,b=b%a,a
    lcm//=b
    print(lcm)
