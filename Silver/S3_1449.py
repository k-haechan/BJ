# 수리공 항승, 2024년 3월 1일 19:47:18, 31120kb, 40ms, 166b
n,l=map(int,input().split())
A=sorted(map(int,input().split()))
answer=0
point=0
for a in A:
    if point-a<0.5:
        point=a-0.5+l
        answer+=1
print(answer)
