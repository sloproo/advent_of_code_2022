def taakse(lista: list, kohta: int) -> int:
    nakyvia = 0
    for i in range(kohta-1, -1, -1):
        if lista[i] < lista[kohta]:
            nakyvia += 1
        elif lista[i] >= lista[kohta]:
            nakyvia += 1
            return nakyvia
    return nakyvia

def eteen(lista: list, kohta: int) -> int:
    nakyvia = 0
    for i in range(kohta+1, len(lista)):
        if lista[i] < lista[kohta]:
            nakyvia += 1
        elif lista[i] >= lista[kohta]:
            nakyvia += 1
            return nakyvia
    return nakyvia

def pystylista(matriisi: list, x: int) -> list:
    return [matriisi[y][x] for y in range(len(matriisi))]

def nakyman_pisteet(matriisi: list, y: int, x: int) -> int:
    vasemmalla = taakse(matriisi[y], x)
    oikealla = eteen(matriisi[y], x)
    ylhaalla = taakse(pystylista(matriisi, x), y)
    alhaalla = eteen(pystylista(matriisi, x), y)
    return vasemmalla * oikealla * ylhaalla * alhaalla

with open("data.txt") as f:
    m = []
    for r in f:
        m.append([int(puu) for puu in r.strip()])

paras_nakyma = 0
for y in range(len(m)):
    for x in range(len(m[y])):
        if nakyman_pisteet(m, y, x) > paras_nakyma:
            paras_nakyma = nakyman_pisteet(m, y, x)

print(paras_nakyma)