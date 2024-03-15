# 평범한 배낭, 2024년 2월 20일 12:56:41, 39608kb, 3300ms, 198b
n,k = map(int,input().split())
bag=[0]*(k+1)
for _ in range(n):
    w,v=map(int,input().split())
    tmp=bag.copy()
    for w_ in range(w,k+1):
        bag[w_]=max(bag[w_],v+tmp[w_-w])
print(bag[k])
