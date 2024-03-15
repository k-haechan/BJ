# 좌표 압축, 2023년 8월 9일 16:31:36, 154804kb, 1848ms, 195b
# 좌표 압축
import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
array=sorted(set(a))
x={n:i for i,n in enumerate(array)}
for i in a:
    print(x[i],end=" ")
