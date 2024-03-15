# 열 개씩 끊어 출력하기, 2024년 3월 2일 23:06:11, 31120kb, 44ms, 95b
s=input()
idx=0
for _ in range(len(s)//10):
    print(s[idx:idx+10])
    idx+=10
print(s[idx:])
