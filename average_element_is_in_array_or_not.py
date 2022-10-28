a=int(input())
b=list(map(int,input().split()))
s=sum(b)
c=s//a
if c in b:
    print(True)
else:
    print(False)