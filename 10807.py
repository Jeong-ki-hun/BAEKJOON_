n = int(input())
k = list(map(int,input().split()))
c = int(input())

cnt =0
for i in k:
    if c==i:
        cnt+=1

print(cnt)

