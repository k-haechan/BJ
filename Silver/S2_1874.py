# 스택 수열, 2023년 9월 4일 16:39:47, 36696kb, 192ms, 441b
import sys
input=sys.stdin.readline
n=int(input())
l=[int(input()) for _ in range(n)]
num=1
s=[]
answer=[]
for i in range(n):
    if l[i]>=num:
        while l[i]>=num:
            s.append(num)
            answer.append('+')
            num+=1
                
        s.pop()
        answer.append('-')
    else:
        if s.pop()!=l[i]:
            print('NO')
            exit()
        answer.append('-')

for x in answer:
    print(x)
