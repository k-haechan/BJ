# 숫자 카드 2, 2024년 2월 23일 17:02:32, 114896kb, 740ms, 213b
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

d={}
for a in A:
    if a in d:
        d[a]+=1
    else:
        d[a]=1

print(*[d[b] if b in d else 0 for b in B])
