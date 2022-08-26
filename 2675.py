n = int(input())

for v in range(n):
    a,b = input().split()
    for i in b:
        print(i*int(a),end="")
    print()