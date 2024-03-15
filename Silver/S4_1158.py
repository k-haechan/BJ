# 요세푸스 문제, 2024년 2월 29일 04:11:51, 31120kb, 44ms, 215b
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
A=list(range(1,n+1))

answer=[]
idx=0
for i in range(n):
    idx=(idx+k-1)%len(A)
    answer.append(str(A.pop(idx)))

print(f"<{', '.join(answer)}>")
