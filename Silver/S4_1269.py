# 대칭 차집합, 2023년 8월 9일 20:18:18, 81488kb, 216ms, 138b
# 대칭 차집합

a,b = map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))

print(a+b-len(A&B)*2)

