# 암호 만들기, 2024년 3월 2일 21:12:37, 31120kb, 44ms, 465b
from itertools import combinations
l,c=map(int,input().split())
A=sorted(input().split())
answer=[]
def check(S):
    vowel={'a','e','i','o','u'}
    v_cnt=0
    c_cnt=0
    for s in S:
        if s not in vowel:
            c_cnt+=1
        else:
            v_cnt+=1
    if c_cnt>=2 and v_cnt>=1:
        return True
    else:
        return False



for x in combinations(A,l):
    if check(x):
        answer.append(x)
for ans in answer:
    print(''.join(ans))
