# 나무 자르기, 2024년 2월 23일 17:43:31, 144340kb, 4412ms, 329b
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
Trees=list(map(int,input().rstrip().split()))
s,e=0,max(Trees)

while s<=e:
    cutter=(s+e)//2
    height=0
    for tree in Trees:
        if tree>cutter:
            height+=tree-cutter
    if height>=m:
        s=cutter+1
    else:
        e=cutter-1

print(e)
