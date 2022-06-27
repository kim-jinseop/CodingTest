import sys

n, m = map(int,sys.stdin.readline().split())

book = []
book_dick = {}
for x in range(n) :
    data = sys.stdin.readline().strip()
    book.append(data)
    book_dick[data] = x+1
    
for _ in range(m) :
    q = sys.stdin.readline().strip()
    
    if q.isnumeric() :
        q = int(q)
        print(book[q-1])
    else :
        print(book_dick[q])

