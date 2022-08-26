natual_num = set(range(1,10001))
sam = set()

for i in natual_num:
    for j in str(i):
        i += int(j)
    sam.add(i)


self_number = sorted(natual_num - sam)

for self in self_number:
    print(self)