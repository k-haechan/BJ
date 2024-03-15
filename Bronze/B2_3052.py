# 나머지, 2022년 1월 28일 23:24:15, 30864kb, 80ms, 77b
a=[int(input()) for _ in range(10)]
b=map(lambda x:x%42,a)
print(len(set(b)))
