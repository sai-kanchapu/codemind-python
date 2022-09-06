a=int(input())
n=1
s=0
while n<a:
    if a%n==0:
        s=s+n
    n=n+1
print(a<s)
    