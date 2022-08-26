def num(i):
    has = 0
    for num in range(1,i+1):
        numlist = list(map(int,str(num)))
        if num < 100:
            has +=1
        elif numlist[0] - numlist[1] == numlist[1] - numlist[2]:
            has += 1
    return has


i = int(input())

print(num(i))

