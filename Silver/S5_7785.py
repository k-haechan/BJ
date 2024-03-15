# 회사에 있는 사람, 2023년 8월 9일 18:44:24, 43104kb, 208ms, 275b
import sys
input = sys.stdin.readline

n=int(input())
log={}
for _ in range(n):
    name, state = input().split()
    if state=='enter':
        log[name]=1
    else:
        log[name]=0
for name in sorted([name for name in log if log[name]==1],reverse=True):
    print(name)
