a=int(input())
for i in range(a):
    n=int(input())
    b=list(map(int,input().strip().split()))
    x=b[n-1]
    if x==max(b):
        print(0)
    else:
        print(max(b)-min(b))