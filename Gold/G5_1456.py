# 거의 소수, 2023년 9월 7일 17:25:06, 135656kb, 3280ms, 403b
a,b = map(int,input().split())
A=[True]*10000000 # 256MB는 거뜬하다
P=[]
for i in range(2,int(len(A)**(0.5))+1):
    if A[i]==False:
        continue
    
    for j in range(i+i,len(A),i):
        A[j]=False
P=[i for i in range(2,len(A)) if A[i]==True]

cnt=0
for p in P:
    sum=0
    tmp=p*p
    while tmp<a:
        tmp*=p

    while tmp<=b:
        sum+=1
        tmp*=p
    cnt+=sum
print(cnt)
