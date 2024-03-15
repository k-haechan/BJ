# 수 찾기, 2024년 2월 23일 16:47:24, 46712kb, 468ms, 511b
# 수 찾기
# n=m=10,0000. 절대로 for문 2개로 풀 수 없다.

n=int(input())
n_list=sorted(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))



def binSearch(target,s,e):
    if s==e:
        if n_list[s]!=target:
            print(0)
            return
    m=(s+e)//2
    if target == n_list[m]:
        print(1)
        return 
    elif target<n_list[m]:
        binSearch(target,s,m)
    else:
        binSearch(target,m+1,e)

for x in m_list:
    binSearch(x,0,n-1)
    
