# 소수&팰린드롬, 2023년 9월 7일 22:05:47, 41412kb, 272ms, 536b
# 소수 & 팬린드롬 수 중에서 최소값 찾기
# O(n)
# 
n=int(input())
size=1_300_000

A=[True]*(size+1)
A[1]=False
def findPrime(A):
    global size
    for i in range(2,int(size**(0.5))+1):
        if A[i]:
            for j in range(i+i,size+1,i):
                A[j]=False

def isPal(x):
    x=str(x)
    n=len(x)
    for i in range(n//2):
        if x[i]!=x[-i-1]:
            return False
    return True
findPrime(A)
while True:
    i=n
    if A[i]:
        if isPal(i):
            print(i)
            break
    n+=1

