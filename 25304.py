total = int(input())
time = int(input())

for i in range(time):
    price,amp = input().split(' ')
    price,amp = int(price),int(amp)

    total -= (price*amp)

print("Yes" if total== 0 else "No")
