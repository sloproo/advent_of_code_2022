with open("alku.txt") as f:
    metsa = []
    for r in f:
        metsa.append([int(puu) for puu in r.strip()])

nakyvia = 0

for y in range(len(metsa)):
    if y == 0 or y == len(metsa) - 1:
        continue
    for x in range(len(metsa[y])):
        if x == 0 or x == len(metsa[y]) - 1:
            continue
        if metsa[y][x] > max([metsa[y][vaaka] for vaaka in range(x)]):
            nakyvia += 1
        elif metsa[y][x] > max([metsa[y][vaaka] for vaaka in range(x+1, len(x))]):
            nakyvia += 1
        elif metsa[y][x] > max([puu for puu in metsa[:y][x]]):
            nakyvia += 1
        elif metsa[y][x] > max([puu for puu in metsa[y+1][x]]):
            nakyvia += 1
        

print(f"Näkyviä puita on {nakyvia}")
        
