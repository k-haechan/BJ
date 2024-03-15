# 이항 계수 3, 2023년 9월 2일 17:03:28, 31388kb, 1336ms, 499b
n,k=map(int,input().split())

a,b=1,1
#combi(n,k) = a*(b^-1) == a/b
for i in range(k):
    a=(a*(n-i))%1_000_000_007 
    b=(b*(1+i))%1_000_000_007

# b^-1 구하기(페르마의 소정리)
# b^(p-1)=1 -> b^(p-2)=b^-1
def pow(x,n): # log, 30번 연산하면 됨
    if n==1:
        return x
    elif n==0:
        return 1
    if n%2==1:
        return ((pow(x,n//2)**2)*x)%1_000_000_007
    else:
        return (pow(x,n//2)**2)%1_000_000_007
    
b=pow(b,1_000_000_005)
print((a*b)%1_000_000_007)
