# 종이의 개수, 2023년 9월 1일 20:10:22, 69432kb, 4880ms, 524b
# 종이의 개수
import sys
input = sys.stdin.readline
paper={-1:0,0:0,1:0}
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

def f(arr,n,r,c):
    for i in range(n):
        for j in range(n):
            if arr[r+i][c+j]!=arr[r][c]:
                    for i2 in range(3):
                         for j2 in range(3):
                            f(arr,n//3,r+(n//3)*i2,c+(n//3)*j2)
                    return
    paper[arr[r][c]]+=1
f(arr,n,0,0)
for x in paper:
    print(paper[x])
