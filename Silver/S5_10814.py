# 나이순 정렬, 2023년 8월 9일 16:13:17, 62420kb, 268ms, 194b
# 나이순 정렬
import sys
input=sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
    lst.append(input().split())
for x in sorted(lst,key=lambda x:int(x[0])):
    print(x[0],x[1])
