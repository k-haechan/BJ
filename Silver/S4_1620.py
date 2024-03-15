# 나는야 포켓몬 마스터 이다솜, 2023년 8월 9일 19:28:09, 54948kb, 228ms, 393b
# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a=[]
poketmons={}
for i in range(n):
    poketmons[input().rstrip('\n')]=i+1
poketmons_list=list(poketmons)
for _ in range(m):
    a.append(input().rstrip('\n'))
for tmp in a:
    if tmp.isdigit():
        print(poketmons_list[int(tmp)-1])
    else:
        print(poketmons[tmp])


