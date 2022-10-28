a=int(input())
b=list(map(int,input().split()))
s=sum(b)
c=s/a
print("{:.2f}".format(c))