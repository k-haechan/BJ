# ATM, 2024년 2월 20일 19:18:12, 31120kb, 44ms, 164b
import sys
input=sys.stdin.readline

n=int(input())
A=sorted(map(int,input().split()),reverse=True)
answer=0
for i in range(n):
    answer+=A[i]*(i+1)
print(answer)
