# 알고리즘 수업 - 병합 정렬 1, 2023년 8월 15일 16:51:55, 136904kb, 2872ms, 960b
# 알고리즘 수업 - 병합 정렬 1
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr=list(map(int,input().split()))
answer=[]

def merge(A,p,q,r):
    tmp=[0]*(r-p+1)
    i,j,t = p,q+1,-1
    while i<=q and j<=r:
        if A[i]<=A[j]:
            tmp[t]=A[i]
            t+=1; i+=1
        else:
            tmp[t]=A[j]
            t+=1; j+=1
    while i<=q:
        tmp[t]=A[i]
        t+=1; i+=1
    while j<=r:
        tmp[t]=A[j]
        t+=1; j+=1

    i,t = p,-1
    while i<=r:
        A[i]=tmp[t]
        answer.append(tmp[t])
        i+=1; t+=1

def merge_sort(A,p,r):
    if p<r: # p가 마지막 인덱스가 아니면
        q=(p+r)//2 # q는 절반을 나누는 인덱스
        merge_sort(arr,p,q) # 반으로 분할 후 정렬
        merge_sort(arr,q+1,r) # 반으로 분할 후 정렬
        merge(A,p,q,r) # 정렬된 절반을 다시 합침

merge_sort(arr,0,n-1)
print(answer[k-1] if len(answer)>=k else -1)

