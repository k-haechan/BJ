# 쿼드트리, 2023년 9월 1일 19:59:09, 31256kb, 44ms, 538b
# 쿼드트리
import sys
input = sys.stdin.readline

n=int(input())
arr=[input().rstrip() for _ in range(n)]

def f(arr,n,r,c):
    for i in range(n):
        for j in range(n):
            if arr[r+i][c+j]!=arr[r][c]:
                print('(',end='')
                f(arr,n//2,r,c)#좌상
                f(arr,n//2,r,c+n//2) #우상
                f(arr,n//2,r+n//2,c) #좌하
                f(arr,n//2,r+n//2,c+n//2) #우하
                print(')',end='')
                return
    print(arr[r][c],end='')
f(arr,n,0,0)
print()
