# 점수계산, 2024년 3월 3일 16:53:22, 31120kb, 40ms, 121b
n=int(input())
A=input().replace(' ','').split('0')
answer=0
for a in A:
    answer+=(len(a)*(len(a)+1))//2
print(answer)
