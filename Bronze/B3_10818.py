# 최소, 최대, 2022년 1월 28일 22:57:15, 149440kb, 700ms, 83b
a=int(input())
b=list(map(int,input().split()))
b.sort()
print(b[0],b[a-1],sep=' ')
