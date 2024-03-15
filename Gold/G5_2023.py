# 신기한 소수, 2023년 9월 5일 14:20:58, 31256kb, 6964ms, 380b
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n=int(input())

def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def dfs(s):
    global n
    if not isPrime(s):
        return
    
    if len(str(s))==n:
        return print(s)
    for i in range(1,10,2):
        dfs(10*s+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
