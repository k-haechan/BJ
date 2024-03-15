# 안테나, 2024년 3월 1일 22:18:25, 53652kb, 172ms, 185b
n=int(input())
A=sorted(map(int,input().split()))
idx=n//2
s1=sum(abs(a-A[idx]) for a in A)
if n%2==0:
    s2=sum(abs(a-A[idx-1]) for a in A)
    if s2<=s1:
        idx-=1
print(A[idx])
