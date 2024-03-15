# 색종이 만들기, 2023년 9월 1일 19:44:38, 31256kb, 68ms, 502b
import sys
input = sys.stdin.readline
n=int(input())
arr=[]
w,b=0,0
for _ in range(n):
    arr.append(list(map(int,input().rstrip().split())))

def f(arr,r,c,n):
    global w
    global b
    s=set()
    for i in range(n):
       s.update(set(arr[r+i][c:c+n]))
    if len(s)==2:
        f(arr,r,c,n//2)
        f(arr,r+n//2,c,n//2)
        f(arr,r,c+n//2,n//2)
        f(arr,r+n//2,c+n//2,n//2)
    else:
        if 1 in s:
            b+=1
        else:
            w+=1
f(arr,0,0,n)
print(w)
print(b)
