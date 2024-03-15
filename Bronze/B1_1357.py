# 뒤집힌 덧셈, 2024년 3월 3일 18:02:23, 31120kb, 44ms, 68b
x,y=input().split()
print(int(str(int(x[::-1])+int(y[::-1]))[::-1]))
