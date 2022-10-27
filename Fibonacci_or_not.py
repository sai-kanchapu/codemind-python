def fab(n):
    a=0
    b=1
    c=a+b
    l=[a,b,b]
    while n>c:
        a=b
        b=c
        c=a+b
        l.append(c)
    if n in l:
        print(True)
    else:
        print(False)
n=int(input())
fab(n)