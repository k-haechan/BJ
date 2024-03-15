# 알파벳 개수, 2024년 2월 28일 12:44:52, 31120kb, 40ms, 66b
A=[0]*26
x=ord('a')
for c in input():
    A[ord(c)-x]+=1
print(*A)
