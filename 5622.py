alpha_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()


time = 0

for i in alpha_list:
    for j in i:
        for w in word:
            if w == j:
                time += alpha_list.index(i) + 3
print(time)