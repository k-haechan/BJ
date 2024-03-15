# 크냐?, 2022년 1월 26일 12:16:14, 30864kb, 80ms, 147b
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")
