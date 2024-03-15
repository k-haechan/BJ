# 별 찍기 - 10, 2023년 8월 15일 20:17:26, 35880kb, 148ms, 299b
n=int(input())


def star(r):
    if r==1:
        return '*'
    stars = star(r//3)
    L=[]
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(r//3)+s)
    for s in stars:
        L.append(s*3)
    return L


L=star(n)
for i in range(n):
    print(''.join(L[i]))
