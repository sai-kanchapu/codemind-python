def ad(n):
    sum = 0
    while n>0:
        r = n%10
        sum = sum+r**2
        n = n//10
    if sum>9:
        sum = ad(sum)
    return sum
    
a = int(input())
x = ad(a)
if x==1 or x==7:
    print(True)
else:
    print(False)