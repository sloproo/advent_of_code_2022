import itertools

with open("data.txt") as f:
    tontut = set()
    y = 0
    for r in f:
        for x in range(len(r.strip())):
            if r[x] == "#":
                tontut.add((y, x))
        y += 1

def ilmansuunnat_pahkailyyn() -> str:
    suunnat = "nswenswe"
    i_suunta = 0
    while True:
        i_suunta = i_suunta % 4
        yield suunnat[i_suunta:i_suunta+4]
        i_suunta += 1

def pysytaanko_paikallaan(y: int, x: int) -> bool:
    naapurit = [koords for koords in itertools.product([y-1, y, y+1], [x-1, x, x+1])]
    naapurit.remove((y, x))
    for y_n, y_x in naapurit:
        if (y_n, y_x) in tontut:
            return False
    return True

def arvioi_menosuunta(y: int, x: int, suunnat: str) -> tuple[tuple[int, int], tuple[int, int]]:
    haettavat = {
        "n": [(y-1, x-1), (y-1, x), (y-1, x+1)],
        "s": [(y+1, x-1), (y+1, x), (y+1, x+1)],
        "w": [(y-1, x-1), (y, x-1), (y+1, x-1)],
        "e": [(y-1, x+1), (y, x+1), (y+1, x+1)]
        }
    menosuunnat = {"n": (y-1, x), "s": (y+1, x), "w": (y, x-1), "e": (y, x+1)}
    for s in suunnat:
        for haettava in haettavat[s]:
            if haettava in tontut:
                break
        else:
            return ((y, x), menosuunnat[s])
    return ((y, x), (y, x))

def tulosta(tontut: set) -> None:
    pienin_y = min([tonttu[0] for tonttu in tontut])
    suurin_y = max([tonttu[0] for tonttu in tontut])
    pienin_x = min([tonttu[1] for tonttu in tontut])
    suurin_x = max([tonttu[1] for tonttu in tontut])    
    korkeus = abs(pienin_y - suurin_y)
    leveys = abs(pienin_x - suurin_x)
    matriisi = []
    for _ in range(korkeus+1):
        matriisi.append(["." for __ in range(leveys+1)])
    korjaus_x, korjaus_y = 0, 0
    if pienin_y < 0:
        korjaus_y = -pienin_y
    if pienin_x < 0:
        korjaus_x = -pienin_x
    korjatut_tontut = {(tonttu[0] + korjaus_y, tonttu[1] + korjaus_x) for tonttu in tontut}
    for y, x in korjatut_tontut:
        matriisi[y][x] = "#"
    for rivi in matriisi:
        for merkki in rivi:
            print(merkki, end="")
        print()

anna_suunta = ilmansuunnat_pahkailyyn()

suunnat = next(anna_suunta)
tonttujen_aikeet = {}
aikeet_tonttujen = {}
liikkuneita = True
kierros = 0
while liikkuneita == True:
    liikkuneita = False
    # Mietitään minne menisi
    for y, x in tontut:
        if pysytaanko_paikallaan(y, x):
            tonttujen_aikeet[(y, x)] = (y, x)
            aikeet_tonttujen[((y, x))] = (y, x)
        else:
            vanha, uusi = arvioi_menosuunta(y, x, suunnat)
            tonttujen_aikeet[vanha] = uusi
            if uusi not in aikeet_tonttujen:
                aikeet_tonttujen[uusi] = [vanha]
            else:
                aikeet_tonttujen[uusi].append(vanha)
    # Liikutaan
    uudet_tontut = set()
    for tonttu in tonttujen_aikeet:
        if len(aikeet_tonttujen[tonttujen_aikeet[tonttu]]) > 1:
            if tonttu in uudet_tontut:
                raise ValueError("Useampi tonttu sittenkin menossa samalle paikalle")
            else:
                uudet_tontut.add(tonttu)
        else:
            if tonttujen_aikeet[tonttu] in uudet_tontut:
                raise ValueError("Useampi tonttu sittenkin menossa samalle paikalle")
            else:
                uudet_tontut.add(tonttujen_aikeet[tonttu])
                liikkuneita = True
    # Valmistellaan seuraava kierros
    kierros += 1
    tontut = uudet_tontut.copy()
    tonttujen_aikeet = {}
    aikeet_tonttujen = {}
    suunnat = next(anna_suunta)
    

pienin_y = min([tonttu[0] for tonttu in tontut])
suurin_y = max([tonttu[0] for tonttu in tontut])
pienin_x = min([tonttu[1] for tonttu in tontut])
suurin_x = max([tonttu[1] for tonttu in tontut])
korkeus = abs(pienin_y-suurin_y) + 1
leveys = abs(pienin_x-suurin_x) + 1


print(f"y = {pienin_y} - {suurin_y} => korkeus = {abs(pienin_y-suurin_y)}")
print(f"x = {pienin_x} - {suurin_x} => leveys = {abs(pienin_x-suurin_x)}")
print(f"Tonttuja on {len(tontut)}")
print(f"Korkeus: {korkeus} , leveys: {leveys} , kerrottuna {korkeus * leveys}")
print(f"Vapaita ruutuja = {korkeus * leveys} - {len(tontut)} = {korkeus * leveys - len(tontut)}")
pass

print(f"Yksikään tonttu ei liikkunut, kierros oli {kierros}")