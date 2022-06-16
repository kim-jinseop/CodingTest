n = input()
sum = 0
dial_chr = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for chr in n :
    for i in range(len(dial_chr)) :
        if chr in dial_chr[i] :
            sum += i+1

print(sum) 