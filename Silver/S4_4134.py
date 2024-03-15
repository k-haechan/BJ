# 다음 소수, 2023년 8월 10일 01:12:39, 31256kb, 2564ms, 379b
# 다음 소수
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    if n<=1:
        print(2)
        continue
    while True:
        tag=True
        for i in range(2,int(n**(0.5))+1):
            if n%i==0:
                tag=False
                break
        if tag:
            break
        else:
            n+=1
    print(n)


