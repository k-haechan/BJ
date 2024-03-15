# 음계, 2024년 3월 3일 14:40:23, 31120kb, 40ms, 157b
A=list(map(int,input().split()))
if A==list(range(1,9)):
    print('ascending')
elif A==list(range(8,0,-1)):
    print('descending')
else:
    print('mixed')
