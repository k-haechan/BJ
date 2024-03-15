# 단어 정렬, 2023년 8월 9일 15:32:54, 36532kb, 92ms, 202b
# 단어 정렬
import sys
input = sys.stdin.readline
n=int(input())
words=set()
for _ in range(n):
    words.add(input().rstrip('\n'))
for word in sorted(words,key=lambda x:(len(x),x)):
    print(word)
