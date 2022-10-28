n=int(input())
l=list(map(int,input().split()))
o=0
for i in l:
    if i%2==1:
        o=o+i
print(o)