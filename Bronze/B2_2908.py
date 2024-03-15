# 상수, 2022년 2월 2일 14:16:37, 30840kb, 64ms, 76b
a=input().split()
b=int(a[0][::-1])
c=int(a[1][::-1])
print(b if b>c else c)
