# 스택, 2024년 2월 29일 14:04:42, 31120kb, 48ms, 380b
import sys
input = sys.stdin.readline

stack=[]
n=int(input())
for _ in range(n):
    a=input().rstrip()
    if a[:3]=='pus':
        stack.append(a.split()[-1])
    elif a[:3]=='pop':
        print(stack.pop() if stack else -1)
    elif a=='size':
        print(len(stack))
    elif a=='empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
