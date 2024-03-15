# 서로 다른 부분 문자열의 개수, 2023년 8월 9일 20:28:05, 240848kb, 516ms, 172b
# 서로 다른 부분 문자열의 개수
s=input()
n=len(s)
answer=set()
for i in range(1,n+1):
    for j in range(n+1-i):
        answer.add(s[j:j+i])
print(len(answer))
