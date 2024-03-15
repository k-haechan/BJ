# 좋다, 2023년 9월 1일 13:43:11, 31256kb, 1260ms, 521b
n=int(input())
l=sorted(map(int,input().split()))
ans=0
# t_idx=0

for t_idx in range(n):
    s_idx=0
    e_idx=n-1
    while s_idx<e_idx:
        if t_idx==e_idx:
            e_idx-=1
            continue
        if t_idx==s_idx:
            s_idx+=1
            continue
        if l[s_idx]+l[e_idx]<l[t_idx]: # 두 수의 합이 더 작으면
            s_idx+=1
        elif l[s_idx]+l[e_idx]>l[t_idx]: # 두 수의 합이 더 크면
            e_idx-=1
        else:
            ans+=1
            break
print(ans)
