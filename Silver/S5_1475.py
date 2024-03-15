# 방 번호, 2024년 2월 28일 12:52:36, 31120kb, 44ms, 205b
number=list(map(int,list(input())))
A=[0]*10
for n in number:
    A[n]+=1
if A[6]>A[9]:
    d=(A[6]-A[9])//2
    A[6]-=d
    A[9]+=d
if A[9]>A[6]:
    d=(A[9]-A[6])//2
    A[9]-=d
    A[6]+=d
print(max(A))
