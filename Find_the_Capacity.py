a,b,c=map(int,input().split())
cap=2*a*b*c*512
d=str(cap//1024)
print(d+"KB")