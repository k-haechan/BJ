# 손익분기점, 2022년 2월 4일 16:29:44, 30860kb, 64ms, 80b
a=list(map(int,input().split()))
print(a[0]//(a[2]-a[1])+1 if a[2]>a[1] else -1)
