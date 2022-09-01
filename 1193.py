n = int(input())

line = 0
max_num = 0

while n > max_num:
    line += 1
    max_num +=line

diff = max_num - n

if line % 2 ==0:
    top = line - diff
    under = diff +1
else:
    top = diff +1 
    under = line - diff

print(f'{top}/{under}')