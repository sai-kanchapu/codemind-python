def prime(a):
    sum=0
    for i in range (1,a+1):
        if a%i==0:
            sum+=1
    if sum==2:
        return True
    else:
        return False
a=int(input())
mp=True
if prime(a)==True:
    while a>0:
        r=a%10
        if prime(r)==False:
            mp=False
            break
        a=a//10
    if mp==True:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")