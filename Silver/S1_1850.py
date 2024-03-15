# 최대공약수, 2023년 9월 11일 23:27:54, 41020kb, 48ms, 128b
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
a,b=map(int,input().split())
print('1'*gcd(a,b))
