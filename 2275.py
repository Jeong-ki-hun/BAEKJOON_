t = int(input())

for i in range(t):
    floor = int(input())
    ho = int(input())
    f = [x for x in range(1,ho+1)]
    for k in range(floor):
        for j in range(1,ho):
            f[j] += f[j-1]
    print(f[-1])

