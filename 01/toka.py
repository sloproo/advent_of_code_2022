with open("input.txt") as f:
    kalorit = []
    
    tonttu = 0
    for i in f:
        i = i.strip()
        if i != "":
            tonttu += int(i)
        else:
            kalorit.append(tonttu)
            tonttu = 0

print(max(kalorit))

print(sorted(kalorit, reverse=True)[0])
print(sorted(kalorit, reverse=True)[1])
print(sorted(kalorit, reverse=True)[2])

print(sum(sorted(kalorit, reverse=True)[0:3]))
