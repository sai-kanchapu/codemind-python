def palindrome(a):
    rev=0
    t=a
    while a>0:
        r=a%10
        rev=rev*10+r
        a=a//10
    if t==rev:
        print("True")
    else:
        print("False")
a=int(input())
palindrome(a)