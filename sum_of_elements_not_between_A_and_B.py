a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in b:
    if i<c or i>d:
        s=s+i
print(s)