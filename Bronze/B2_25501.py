# 재귀의 귀재, 2023년 8월 11일 15:10:23, 31316kb, 472ms, 329b
# 재귀의 귀재
import sys
input = sys.stdin.readline

t=int(input())
def rec(s,cnt,l,r):
    cnt[0]+=1
    if l-r>=0:
        return 1
    elif s[l]!=s[r]:
        return 0
    else:
        return rec(s,cnt,l+1,r-1)
for _ in range(t):
    count=[0]
    s=input().rstrip()
    print(rec(s,count,0,len(s)-1),count[0])
        
