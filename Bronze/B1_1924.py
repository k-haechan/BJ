# 2007년, 2024년 3월 3일 02:01:35, 31120kb, 44ms, 158b
x,y=map(int,input().split())
M=[31,28,31,30,31,30,31,31,30,31,30,31]
D=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
day=(sum(M[:x-1])+y-1)%7
print(D[day])
