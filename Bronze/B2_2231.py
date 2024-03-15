# 분해합, 2022년 2월 15일 11:43:55, 30864kb, 68ms, 170b
n = input()
l = len(n)
n = int(n)

for x in range(n - 9 * l, n):
    if x >= 1 and x + sum(map(int, list(str(x)))) == n:
        print(x)
        break
else:
    print(0)
