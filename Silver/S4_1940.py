# 주몽, 2023년 8월 31일 22:52:50, 32276kb, 52ms, 224b
n=int(input())
m=int(input())
l=sorted(map(int,input().split()))

s,e=0,n-1
ans=0

while s<e:
    if l[s]+l[e]==m:
        ans+=1
        s+=1
        e-=1
    elif l[s]+l[e]<m:
        s+=1
    else:
        e-=1
print(ans)
