# 요세푸스 문제 0, 2023년 8월 11일 00:22:57, 31256kb, 44ms, 251b
# 요세푸스 문제 0
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
lst= list(range(1,n+1))
answer=[]
idx=0
for i in range(n):
    idx=(idx+(k-1))%(n-i)
    answer.append(str(lst.pop(idx)))
ret='<'+', '.join(answer)+'>'
print(ret)
