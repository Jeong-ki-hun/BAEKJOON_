a,b,c = map(int,input().split())


if b >=c:
    print(-1)
elif b < c:
    d = c - b
    break_point = a // d
    print(break_point+1)