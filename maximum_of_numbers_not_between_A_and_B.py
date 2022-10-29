a=int(input())
l=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
for i in l:
    if i<c or i>d:
        e.append(i)
if len(e)>0:
    print(max(e))
else:
    print(-1)