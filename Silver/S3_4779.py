# 칸토어 집합, 2023년 8월 15일 17:33:10, 32292kb, 44ms, 163b
while True:
    try:
        N=int(input())
        a='-'
        for _ in range(N):
            a = a + ' '*len(a) + a
        print(a)
    except:
        break

