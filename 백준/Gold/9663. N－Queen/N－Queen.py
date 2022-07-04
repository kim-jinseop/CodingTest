import sys

n = int(sys.stdin.readline())
chk = [0] * n
cnt = 0

def backtracking(x) :
    global cnt
    if x==n :
        cnt += 1
        return 

    for i in range(n) :
        chk[x] = i

        if queen_chk(x) :
            backtracking(x+1)

def queen_chk(c) :
    for i in range(c) :
        if chk[i] == chk[c] or abs(chk[c]-chk[i]) == c-i:
            return False
            
    return True

backtracking(0)
print(cnt)