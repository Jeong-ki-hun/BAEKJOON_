a,b = map(int,input().split())
t = int(input())
a += t // 60
b += t % 60
if 60<=b:
    a +=1
    b -= 60
if 24<=a:
    a -= 24
print(a,b)