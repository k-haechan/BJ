# 기타 레슨, 2023년 9월 6일 02:49:32, 42340kb, 636ms, 538b
N,M = map(int,input().split())
A=list(map(int,input().split()))
s=max(A) # 하나의 영상을 담을 수 있는 최소 크기
e=sum(A) # 전체의 영상을 담을 수 있는 최소 크기
while s<=e: # 
    m=(s+e)//2
    sum=0
    cnt=0
    for i in range(N):
        if sum+A[i] > m:
            cnt+=1
            sum=0
        sum+=A[i]
    if sum != 0:
        cnt +=1
    if cnt > M:
        s = m+1 #m은 아니라면
    else: # cnt <= M -> cnt == M이더라도,
        e = m-1 #더 잘게 쪼갤 수 있는지 확인.
print(s)
