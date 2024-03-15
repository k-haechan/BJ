# K번째 수, 2024년 2월 23일 16:20:38, 31120kb, 1016ms, 451b
n,k=int(input()),int(input())
# 정의역은 1~k
# m부터 찾는 것.(2분탐색)
# 만약 자기보다 작은 수가 k개 보다 많으면 다음을 의심한다.
s,e=1,k
while s<=e:
    m=(s+e)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(n,m//i)
    if cnt<k: # m일 때 더 작다? 정의역은 다시 m+1부터
        s=m+1
    else:     # m은 k일 때 s==e==k 마지막에 e=k-1, s=k로 조건이 끝난다.
        e=m-1
print(s)
