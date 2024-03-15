# 제곱 ㄴㄴ 수, 2023년 9월 8일 02:23:09, 39068kb, 892ms, 234b
min,max=map(int,input().split())

arr=[1]*(max-min+1)

for i in range(2,int(max**(0.5))+1):
    pow=i**2
    idx=min//pow
    if min%pow!=0:
        idx+=1
    for j in range(idx,(max//pow)+1):
        arr[pow*j-min]=0
print(sum(arr))
