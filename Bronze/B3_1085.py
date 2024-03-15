# 직사각형에서 탈출, 2022년 2월 9일 21:32:50, 30864kb, 68ms, 56b
x,y,w,h=map(int,input().split())
print(min(w-x,x,h-y,y))
