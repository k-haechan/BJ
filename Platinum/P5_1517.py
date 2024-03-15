# 버블 소트, 2023년 9월 5일 01:30:05, 93508kb, 2292ms, 718b
n=int(input())
A=list(map(int,input().split()))
tmp=[0]*n
result = 0 

def mergeSort(s,e):
    global result

    if s+1>e:
        return
    
    m=(s+e)//2
    mergeSort(s,m)
    mergeSort(m+1,e)

    for i in range(s,e+1):
        tmp[i]=A[i]

    k=s
    idx1=s
    idx2=m+1

    while idx1<=m and idx2 <=e:
        if tmp[idx1]>tmp[idx2]:
            A[k]=tmp[idx2]
            result += (idx2-k)
            k+=1
            idx2+=1
        else:
            A[k]=tmp[idx1]
            k+=1
            idx1+=1
        
    while idx1<=m:
        A[k]=tmp[idx1]
        idx1+=1
        k+=1

    while idx2<=e:
        A[k]=tmp[idx2]
        idx2+=1
        k+=1
    
mergeSort(0,n-1)
print(result)
            
