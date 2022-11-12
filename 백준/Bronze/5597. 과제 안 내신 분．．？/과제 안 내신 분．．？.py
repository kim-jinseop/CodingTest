n = []
for _ in range(28) :
    n.append(int(input()))

result = []
for i in range(1, 31) :
    if i not in n :
        result.append(i)

print(min(result))
print(max(result))