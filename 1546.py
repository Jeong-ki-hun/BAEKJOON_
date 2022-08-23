times = int(input())
arr = list(map(int,input().split()))
max_ = max(arr)

a = []
for i in range(times):
    a.append(arr[i]/max_*100)
b =(sum(a))/times

print(b)