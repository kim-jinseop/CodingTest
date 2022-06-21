import sys
cnt=0
t = int(input())
for i in range(666, sys.maxsize): #sys.maxint는 python3에서 사라짐.
    if('666' in str(i)):
        cnt+=1
        if(cnt==t):
            print(i)
            exit()
