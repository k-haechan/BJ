# 대표값2, 2023년 7월 3일 11:31:34, 31388kb, 44ms, 98b
a=[0]*5
for i in range(5):
    a[i]=int(input())
a.sort()
mean=int(sum(a)/len(a))
print(mean,a[2])
