dice = list(map(int,input().split()))
count = 0
if dice[0] == dice[1] :
    count += 1
    save = dice[0]
if dice[0] == dice[2] :    
    count += 1
    save = dice[0]
if dice[1] == dice[2] :
    count += 1
    save = dice[1]

if count== 3 :
    print(10000 + dice[0]*1000)
elif count == 1 :
    print(1000 + save * 100)
else :
    print(max(dice) * 100)