data = input()
croatia = 0

for index in range(len(data)) :
    if data[index] in ['=', '-'] :
        if data[index-2:index] == 'dz' :
            croatia += 1
        croatia += 1
    
    elif data[index] == 'j' :
        if data[index-1] in ['l', 'n'] :
            croatia += 1

print(len(data)-croatia)