# IPv6, 2023년 8월 21일 14:26:41, 31256kb, 40ms, 386b
# IPv6

import sys
input=sys.stdin.readline

IPv6=input().rstrip().split(':')
# 1. ::이 존재하는 경우
if IPv6[0]=='':
    IPv6=IPv6[1:]
elif IPv6[-1]=='':
    IPv6.pop()
l=len(IPv6)

if '' in IPv6:
    i=IPv6.index('')
    IPv6=IPv6[:i+1]+['']*(8-l)+IPv6[i+1:]
# 2. 패딩
for i in range(8):
    l=len(IPv6[i])
    if l!=4:
        IPv6[i]='0'*(4-l)+IPv6[i]
print(':'.join(IPv6))
