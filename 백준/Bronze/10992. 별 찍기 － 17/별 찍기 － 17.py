from sys import stdin 

n = int(stdin.readline())

for x in range(n) :
    if x!=(n-1) :
        for i in range(n) :
            if i==n-1-x :
                print('*',end='')
            else :
                print(' ',end='')
        
        if x != 0 :
            for i in range(n-1) :
                if i==(x-1) :
                    print('*',end='')
                    break
                else :
                    print(' ',end='')
    else :
        print('*' * (n*2-1))

    print('\n',end='')