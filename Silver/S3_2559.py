# 수열, 2023년 8월 23일 22:48:36, 40292kb, 84ms, 193b
# 수열
n,k = map(int,input().split())
arr = list(map(int,input().split()))
lst=[0]*(n-k+1)
lst[0]=sum(arr[:k])
for i in range(1,n-k+1):
    lst[i]=lst[i-1]-arr[i-1]+arr[i+k-1]
print(max(lst))
