# 사과나무, 2023년 7월 10일 13:53:11, 42172kb, 96ms, 217b
n=int(input())
L=sorted(map(int,input().split()))
# 1 3 1 3 1 => 9 -> 1*3 2*3
m=sum(map(lambda x:x//2,L))
if sum(L)%3!=0:
    print("NO")
else:
    if (sum(L)//3)<=m:
        print("YES")
    else:
        print("NO")
