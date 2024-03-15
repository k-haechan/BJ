# 회의실 배정, 2024년 2월 20일 19:12:06, 59852kb, 272ms, 229b
import sys
input = sys.stdin.readline

n=int(input())
A=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:(x[1],x[0]))
end=0
answer=0
for s,e in A:
    if s>=end:
        answer+=1
        end=e
print(answer)
