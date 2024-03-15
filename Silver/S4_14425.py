# 문자열 집합, 2023년 8월 9일 18:32:15, 36688kb, 892ms, 151b
n,m = map(int,input().split())
s1=set()
cnt=0
for _ in range(n):
    s1.add(input())
for _ in range(m):
    if input() in s1:
        cnt+=1
print(cnt)
