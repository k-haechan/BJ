# 숫자 카드, 2024년 2월 18일 01:36:15, 121528kb, 596ms, 124b
input()
A=set(map(int,input().split()))
input()
B=list(map(int,input().split()))
C=[1 if x in A else 0 for x in B]
print(*C)
