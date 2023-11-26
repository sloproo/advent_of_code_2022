import copy, time

alku = time.time()

def lue_lumet(kartta: list) -> list:
    lumet = []
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            ruutu = kartta[y][x]
            if ruutu != "." and ruutu != "#":
                lumet.append((y, x, ruutu))
    return lumet

def aloituskoordinaatti(kartta: list) -> tuple[int, int]:
    for x in range(len(kartta[0])):
        if kartta[0][x] == ".":
            return (0, x)

def maalikoordinaatti(kartta: list) -> tuple[int, int]:
    for x in range(len(kartta[-1])):
        if kartta[-1][x] == ".":
            return (len(kartta)-1, x)

def puhalla(lumet: list) -> tuple[list, list, list, list]:
    uudet = []
    for y, x, suunta in lumet:
        if suunta == "^":
            uudet.append((y-1, x, suunta)) if y > 1 else uudet.append((len(kartta) -2, x, suunta))
        elif suunta == ">":
            uudet.append((y, x+1, suunta)) if x < len(kartta[y]) -2 else uudet.append((y, 1, suunta))
        elif suunta == "v":
            uudet.append((y+1, x, suunta)) if y < len(kartta) -2 else uudet.append((1, x, suunta))
        elif suunta == "<":
            uudet.append((y, x-1, suunta)) if x > 1 else uudet.append((y, len(kartta[y]) -2, suunta))
    return uudet

def nayta(omat: set[int, int], lumet: list, vanha:list) -> list:
    kartta = []
    kartta.append(vanha[0])
    for _ in range(len(vanha)-2):
        kartta.append(["#"] + ["." for __ in range(len(vanha[0]) -2)] + ["#"])
    kartta.append(vanha[-1])
    for y, x, suunta in lumet:
        if kartta[y][x] == ".":
            kartta[y][x] = suunta
        elif type(kartta[y][x]) == int:
            kartta[y][x] += 1
        else:
            kartta[y][x] = 2
    # Ihtet kartalle
    for oma_y, oma_x in omat:
        if kartta[oma_y][oma_x] == ".":
            kartta[oma_y][oma_x] = "I"
    for r in kartta:
        rivi_string = ""
        for m in r:
            rivi_string += str(m)
        print(rivi_string)
    print()
    kartta[oma_y][oma_x] = "."
    for y_siiv in range(len(kartta)):
        for x_siiv in range(len(kartta[y_siiv]) -1):
            if kartta[y_siiv][x_siiv] == "I":
                kartta[y_siiv][x_siiv] = "."
    return kartta

def menosuunnat(omat: set[int, int], lumet: list, kartta: list) -> list:
    mahdolliset = set()
    for oma in omat:
        y, x = oma[0], oma[1]
        ehdokkaat = [(y, x+1), (y+1, x), (y-1, x), (y, x-1), (y, x)]
        lumikoordinaatit = [lumi[0:2] for lumi in lumet]
        for y_m, x_m in ehdokkaat:
            if (y_m, x_m) in mahdolliset:
                continue
            if y_m < 0 or y_m > len(kartta) - 1:
                continue
            if x_m < 1 or x_m > len(kartta[y_m]) -2:
                continue
            elif (y_m == 0 and kartta[y_m][x_m] != ".") or (
                y_m == len(kartta) -1 and kartta[y_m][x_m] != "."):
                continue
            elif (y_m, x_m) in lumikoordinaatit:
                continue
            else:
                mahdolliset.add((y_m, x_m))
    return mahdolliset

def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        kartta = []
        for r in f:
            rivi = []
            for m in r.strip():
                rivi.append(m)
            kartta.append(rivi)
    return kartta

kartta = lue("data.txt")
lumet = lue_lumet(kartta)
k_tontut = {aloituskoordinaatti(kartta)}
maali = maalikoordinaatti(kartta)

kierros = 0
maaleja = 0

while True:
    if maali in k_tontut:
        maaleja += 1
        print(f"Maali saavutettiin {maaleja}. kertaa kierroksen {kierros} jälkeen")
        loppu = time.time()
        print(f"Aikaa kulunut tähän mennessä {loppu-alku} s")
        if maaleja == 3:
            break
        else:
            print("Lähdetään toiseen suuntaan")
            if maaleja % 2 == 1:
                k_tontut = {maalikoordinaatti(kartta)}
                maali = aloituskoordinaatti(kartta)
            else:
                k_tontut = {aloituskoordinaatti(kartta)}
                maali = maalikoordinaatti(kartta)

    nayta(k_tontut, lumet, kartta)
    lumet = puhalla(lumet)
    k_tontut = menosuunnat(k_tontut, lumet, kartta)
    kierros += 1
