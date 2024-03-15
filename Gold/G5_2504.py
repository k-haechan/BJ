# 괄호의 값, 2024년 3월 1일 16:18:14, 34044kb, 64ms, 851b
import sys
from collections import deque

input=sys.stdin.readline
        
s=input().rstrip()
A=[]
try:
    for c in s:
        if c=='(':
            A.append(c)
        elif c=='[':
            A.append(c)
        elif c==')':
            tmp=1
            while True:
                x=A.pop()
                if x=='(':
                    tmp*=2
                    break
                if tmp==1:
                    tmp=x
                else:
                    tmp+=x
            A.append(tmp)
        
        elif c==']':
            tmp=1
            while True:
                x=A.pop()
                if x=='[':
                    tmp*=3
                    break
                if tmp==1:
                    tmp=x
                else:
                    tmp+=x
            A.append(tmp)

    print(sum(A))
except:
    print(0)
