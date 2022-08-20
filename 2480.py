a,b,c = map(int,input().split())
mylist = [a,b,c]
if len(set(mylist)) ==1:
    print(10000+(mylist[0])*1000)
elif len(set(mylist)) ==3:
    print(max(mylist)*100)
else:
    print(1000+(sum(mylist) -sum(set(mylist))) * 100)