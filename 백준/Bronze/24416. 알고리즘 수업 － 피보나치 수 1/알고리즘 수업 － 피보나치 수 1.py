def fib(n) :
    if n == 1 or n == 2 :
        return 1  # 코드1
    else :
        return (fib(n - 1) + fib(n - 2))

n = int(input())

print('{} {}'.format(fib(n),n-2))