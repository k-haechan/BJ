# 평행 우주, 2023년 11월 23일 10:37:54, 68248kb, 228ms, 156b
import math
n=int(input())
A=reversed(list(map(int,input().split())))
x=0
for a in A:
    if a>=x:
        x=a
    else:
        x=math.ceil(x/a)*a
print(x)
