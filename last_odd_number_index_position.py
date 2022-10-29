a=int(input())
l=list(map(int,input().split()))
l.reverse()
for i in range(a):
    if l[i]%2==1:
        b=abs(i-a+1)
        print(b)
        break