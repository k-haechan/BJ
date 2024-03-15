# 오큰수, 2024년 2월 23일 23:06:19, 155536kb, 1080ms, 250b
import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
answer=[-1]*n
stack=[]

for i in range(n):
    while stack and A[stack[-1]]<A[i]:
        answer[stack.pop()]=A[i]
    else:
        stack.append(i)
print(*answer)
