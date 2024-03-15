# 연속합, 2024년 2월 18일 18:29:20, 38828kb, 76ms, 157b
n=int(input())
A=list(map(int,input().split()))
sum=0
M=-float('inf')
for n in A:
    sum+=n
    if M<sum:
        M=sum
    if sum<0:
        sum=0
print(M)
