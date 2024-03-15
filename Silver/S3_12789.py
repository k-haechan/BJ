# 도키도키 간식드리미, 2023년 8월 10일 12:34:53, 34140kb, 68ms, 457b
# 도키도키 간식 드리미
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
array=deque(map(int,input().split()))
stack=[]
cnt=1
while array:
    if stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt+=1
            continue

    x=array.popleft()
    if x==cnt:
        cnt+=1
    else:
        stack.append(x)
if stack==sorted(stack,reverse=True):
    print('Nice')
else:
    print('Sad')

