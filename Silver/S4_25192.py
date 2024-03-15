# 인사성 밝은 곰곰이, 2023년 8월 11일 11:03:51, 42524kb, 88ms, 294b
# 인사성 밝은 곰곰이
import sys
input=sys.stdin.readline

n=int(input())
lst=set()
answer=0
for _ in range(n):
    s=input().rstrip()
    if s=='ENTER':
        if lst:
            answer+=len(lst)
            lst.clear()
    else:
        lst.add(s)
    
answer+=len(lst)
print(answer)
