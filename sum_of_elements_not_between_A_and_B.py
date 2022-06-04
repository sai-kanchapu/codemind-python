a = int(input())
b = list(map(int,input().split()))
x,y = map(int,input().split())
sum = 0
for i in b:
    if i<x or i>y:
        sum = sum+i
print(sum)