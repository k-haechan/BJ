# DNA 비밀번호, 2023년 9월 4일 03:44:35, 33196kb, 696ms, 560b
# DNA 비밀번호
import sys
input = sys.stdin.readline
ls,lp = map(int,input().rstrip().split())
s=input().rstrip()
leastSize=list(map(int,input().rstrip().split()))
answer = 0

lst=['A', 'C', 'G', 'T']
d={x:0 for x in lst}
for i in range(lp):
    d[s[i]]+=1

def check(d,leastSize):
    lst=[d[x] for x in d]
    for i in range(4):
        if lst[i]<leastSize[i]:
            return False
    return True
if check(d,leastSize):
    answer+=1

for i in range(ls-lp):
    d[s[i]]-=1
    d[s[i+lp]]+=1
    if check(d,leastSize):
        answer+=1
print(answer)
