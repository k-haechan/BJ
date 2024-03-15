# 달팽이는 올라가고 싶다, 2022년 2월 5일 15:44:22, 32972kb, 68ms, 88b
import math
a=list(map(int,input().split()))
print(math.ceil((a[2]-a[0])/(a[0]-a[1]))+1)
