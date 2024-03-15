# 다리 놓기, 2024년 2월 18일 01:18:54, 31120kb, 76ms, 168b
T=int(input())
for i in range(T):
    r,n=map(int,input().split())
    div,answer=1,1
    for i in range(r):
        answer*=n-i
        div*=i+1
    print(answer//div)
