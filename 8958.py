times = int(input())

for i in range(times):
    ox_list = list(input())
    score = 0
    sumscore =0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            sumscore += score
        else:
            score = 0

    print(sumscore)
