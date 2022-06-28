n = int(input())

w = []
h = []
total = []
for i in range(6) :
    a,b = map(int,input().split())
    total.append(b)
    if a==1 or a==2 :
        w.append(b)
    else : 
        h.append(b)

w_max = max(w)
h_max = max(h)
w_max_idx = total.index(w_max)
h_max_idx = total.index(h_max)

big_size = w_max * h_max

small1 = abs(total[w_max_idx-1]-total[0 if w_max_idx == 5 else w_max_idx+1])
small2 = abs(total[h_max_idx-1]-total[0 if h_max_idx == 5 else h_max_idx+1])

small_size = small1 * small2

print((big_size-small_size)*n)
