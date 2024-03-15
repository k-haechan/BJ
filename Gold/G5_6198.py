# 옥상 정원 꾸미기, 2024년 3월 1일 17:40:23, 37488kb, 112ms, 347b
import sys
input=sys.stdin.readline

n=int(input())
A=[int(input()) for _ in range(n)][::-1]
answer=[0]*n
stack=[(float('inf'),0)]
for i in range(n):
    cnt=0
    while stack[-1][0]<A[i]: # 볼 수 있는 애들이 있다면
        val,idx=stack.pop()
        cnt+=1
        answer[i]+=answer[idx]+1
    stack.append((A[i],i))
print(sum(answer))
