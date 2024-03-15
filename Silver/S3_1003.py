# 피보나치 함수, 2024년 3월 2일 21:31:40, 31120kb, 40ms, 277b
import sys
input=sys.stdin.readline

fibo=[[0,0] for _ in range(41)]
fibo[0][0]=1
fibo[1][1]=1

for i in range(2,41):
    fibo[i][0]=fibo[i-1][0]+fibo[i-2][0]
    fibo[i][1]=fibo[i-1][1]+fibo[i-2][1]

n=int(input())
for _ in range(n):
    num=int(input())
    print(*fibo[num])
