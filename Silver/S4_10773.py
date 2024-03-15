# 제로, 2023년 8월 10일 02:11:03, 32036kb, 80ms, 194b
# 제로
import sys
input = sys.stdin.readline

k=int(input())
stack=[]
for _ in range(k):
    n=int(input())
    if n!=0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))
