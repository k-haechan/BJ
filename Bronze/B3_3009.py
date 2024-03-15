# 네 번째 점, 2022년 1월 26일 13:06:24, 30860kb, 72ms, 109b
a=[tuple(map(int,input().split())) for _ in range(3)]
print(a[0][0]^a[1][0]^a[2][0],a[0][1]^a[1][1]^a[2][1])

