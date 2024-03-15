# 스택 2, 2023년 8월 10일 02:07:32, 71248kb, 1024ms, 451b
import sys
input = sys.stdin.readline

n=int(input())
stack=[]
for _ in range(n):
    x=input().rstrip('\n')
    if len(x)==1:
        x=int(x)
        if x==2:
            print(stack.pop() if stack else -1)
        elif x==3:
            print(len(stack))
        elif x==4:
            print(1 if not stack else 0)
        elif x==5:
            print(stack[-1] if stack else -1)
        
    else:
        stack.append(int(x.split()[1]))
    
    
