a,b,c=map(int,input().split())
co=0
while a<=b:
    if a%c==0:
        co=co+1
    a=a+1
print(co)
