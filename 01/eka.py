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
