# 괄호, 2023년 8월 10일 02:28:19, 31256kb, 44ms, 455b
# 괄호
import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    s=input().rstrip('\n')
    stack=[]
    Tag=True
    for c in s:
        if c=='(':
            stack.append(c)
        else:
            try:
                if stack.pop()!='(':
                    Tag=False
                    break
            except:
                Tag=False
                break
    if stack:
        Tag=False
    print('YES' if Tag else 'NO')
