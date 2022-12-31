def luo_palikka(korkeus: int) -> list:
    palikat = {"vaaka": [(korkeus + 4, i+2) for i in range(4)],
                "plus": [(korkeus + 5, 2), (korkeus + 5, 3), 
                        (korkeus + 5, 4), (korkeus + 6, 3), (korkeus + 4, 3)],
                "kulma": [(korkeus + 4, 2), (korkeus + 4, 3), (korkeus + 4, 4),
                        (korkeus + 5, 4), (korkeus + 6, 4)],
                "pysty": [(korkeus + 4 + i, 2) for i in range(4)],
                "nelio": [(korkeus + 4, 2), (korkeus + 5, 2),
                        (korkeus + 4, 3), (korkeus + 5, 3)]}
    muodot = palikat.keys()
    i = 0
    while True:
        yield palikat[muoto]
        i += 1
        if i == 5: i = 0

def liikuta(palikka: list, torni: list, suunta: str, baseline: int) -> list:
    for y, x in palikka:
        if suunta == "<":
            if torni[baseline + y][x-1] == "#":
                return palikka
            elif x == -1:
                return palikka
        elif suunta == ">":
            if torni[baseline + y][x+1] == "#":
                return palikka
            elif x == 7:
                return palikka
        else:
            raise KeyError("Mahdoton suunta liikuttaessa")
    if suunta == "<":
        return [(y, x -1) for y, x in palikka]
    elif suunta == ">":
        return [(y, x +1) for y, x in palikka]

def pudota (palikka: list, torni: list, baseline: int) -> tuple[list, list]:
    pysahtyi = False
    for y, x in palikka:
        if torni[y - baseline - 1][x] == "#" or y - 1 == baseline:
            pysahtyi = True
        
    if pysahtyi:
        tyhja_rivi = [[" "] for _ in range(7)]
        for _ in range(4):
            torni.append(tyhja_rivi)
        for y, x in palikka:
                torni[y - baseline][x] = "#"
        for _ in range(4):
            if torni[-1] == tyhja_rivi:
                torni.pop[-1]
        return (torni, [])
    else:
        laskenut_palikka = []
        for y, x in palikka:
            laskenut_palikka.append((y - 1, x))
        return (torni, laskenut_palikka)

def tasoita(torni: list, baseline: int) -> tuple(list, int):
    taysi_rivi = ["#" for _ in range(7)]
    for i in range(len(torni) - 1, 0, -1):
        if torni[i] == taysi_rivi:
            torni = torni[i:]
            baseline += i
            return (torni, baseline)
    return (torni, baseline)

        
"""
Baselinen määritys puuttuu
"""

torni = [["#"] for _ in range(7)]
baseline = 0

muotoilija = luo_palikka()

for i in range(2022):
    palikka = next(muotoilija(baseline + len(torni)))
    while palikka != []:
        palikka = liikuta(palikka, torni, suunta, baseline)
        torni, palikka = pudota(palikka, torni, baseline)
    torni, baseline = tasoita(torni, baseline)


print("Palikat pudotettu\nTorni:")
for i in range(len(torni)):
    print(torni[-i])

print(f"Tornin korkeus = {len(torni) + baseline}")
print(f"(Jäljelläolevan tornin korkeus: {len(torni)} , baseline: {baseline}")