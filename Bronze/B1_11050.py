# 이항 계수 1, 2023년 8월 11일 10:48:53, 31256kb, 40ms, 116b
n,k = map(int,input().split())
answer=1
div=1
for i in range(k):
    answer*=(n-i)
    div*=(i+1)
print(answer//div)
