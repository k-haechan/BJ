# 듣보잡, 2023년 8월 9일 20:15:18, 44060kb, 96ms, 262b
# 듣보잡
import sys
input=sys.stdin.readline
n,m = map(int,input().split())

N=set()
M=set()

for _ in range(n):
    N.add(input().rstrip('\n'))
for _ in range(m):
    M.add(input().rstrip('\n'))

NM=sorted(N&M)
print(len(NM))
for name in NM:
    print(name)

