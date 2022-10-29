a=int(input())
b=list(map(int,input().split()))
b.reverse()
for i in b:
    if i%2==1:
        print(i)
        break