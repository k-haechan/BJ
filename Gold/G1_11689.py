# GCD(n, k) = 1, 2023년 9월 8일 13:55:32, 31256kb, 144ms, 166b
n=int(input())
res=n
for p in range(2,int(n**(0.5))+1):
    if n%p==0:
        res-=res//p
        while n%p==0:
            n//=p
if n!=1:
    res-=res//n
print(res)
