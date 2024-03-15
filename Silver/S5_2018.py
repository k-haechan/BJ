# 수들의 합 5, 2023년 8월 31일 21:55:50, 31256kb, 4456ms, 327b
n=int(input())
start_idx=0
end_idx=1
answer=1

s=1

while end_idx<n: # end_index>=n인 경우. end_index=n-1(마지막 인덱스)인데 s의 크기가 더 작은 경우. 
    if s<=n:
        if s==n:
            answer+=1
        end_idx+=1
        s+=end_idx
    else:
        s-=start_idx
        start_idx+=1

print(answer)
