# 애너그램 만들기, 2024년 2월 29일 13:35:00, 34016kb, 64ms, 236b
import sys
from collections import deque

input=sys.stdin.readline
        
s1=input().rstrip()
s2=input().rstrip()
A=[0]*26
x=ord('a')
for c1 in s1:
    A[ord(c1)-x]+=1
for c2 in s2:
    A[ord(c2)-x]-=1
A=list(map(abs,A))
print(sum(A))
