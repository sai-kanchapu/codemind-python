a,b,c=map(int,input().split())
per=a+b+c
s=per/2
d=(s*(s-a)*(s-b)*(s-c))**0.5
print('{:.2f}'.format(d))