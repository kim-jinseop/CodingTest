from sys import stdin
from heapq import heappush, heappop

t = int(stdin.readline())
for _ in range(t) :
    k = int(stdin.readline())
    aq = [] # 오름차순
    dq = [] # 내림차순
    chk = [0] * k

    for i in range(k) :
        oper, n = stdin.readline().split()
        if oper == "I" :
            heappush(aq, (int(n), i))
            heappush(dq, (-int(n), i))
        else :
            if n== "-1" : # 최소값 삭제
                if aq :
                    chk[heappop(aq)[1]] = 1
            else : # 최대값 삭제
                if dq :
                    chk[heappop(dq)[1]] = 1

            while aq and chk[aq[0][1]] :
                heappop(aq)
            while dq and chk[dq[0][1]] :
                heappop(dq)

    if aq and dq :
        print(-dq[0][0], aq[0][0])
    else :
        print("EMPTY")