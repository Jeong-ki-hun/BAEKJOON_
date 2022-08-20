a,b = [int(i) for i in input().split()]
T = ((a*60 + b-45))
if T<0:
    T = (T + (24*60))
H = T // 60
M = T % 60
print(H,M)
    

