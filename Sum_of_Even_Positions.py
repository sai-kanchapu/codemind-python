n=int(input())
l=list(map(int,input().split()))
o=0
for i in range (n):
    if i%2==1:
        o=o+l[i]
print(o)