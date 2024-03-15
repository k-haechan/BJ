# 나는 요리사다, 2024년 3월 3일 18:00:07, 31120kb, 40ms, 83b
A=[sum(map(int,input().split())) for _ in range(5)]
print(A.index(max(A))+1,max(A))
