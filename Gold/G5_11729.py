# 하노이 탑 이동 순서, 2024년 2월 18일 16:01:37, 31120kb, 852ms, 232b
import sys
input=sys.stdin.readline

def hanoi(n,From,Via,To):
    if n==1:
        print(From,To)
        return
    hanoi(n-1,From,To,Via)
    print(From,To)
    hanoi(n-1,Via,From,To)

n=int(input())
print(2**n-1)
hanoi(n,1,2,3)

