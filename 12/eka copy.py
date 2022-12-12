import string, time, os, copy

def alun_koordinaatit(kartta: list) -> tuple:
    for y in range(len(kartta)):
        if "S" in kartta[y]:
            return (y, kartta[y].index("S"))

def maalin_koordinaatit(kartta: list) -> tuple:
    for y in range(len(kartta)):
        if "E" in kartta[y]:
            return (y, kartta[y].index("E"))

def kirjain_ruudussa(koordinaatit: tuple, kartta:list) -> str:
    return kartta[koordinaatit[0]][koordinaatit[1]]

def ekasta_tokaan(eka: tuple, toka: tuple) -> tuple:
    return (toka[0] - eka[0], toka[1] - eka[1])

def menosuunnat(vektori: tuple) -> tuple:
    if abs(vektori[1]) > abs(vektori[0]):
        if vektori[1] >= 0:
            return "RUDL"
        else:
            return "LUDR"
    else:
        if vektori[0] >= 0:
            return "DRLU"
        else:
            return "URLD"

def paikka_suunnassa(piste: tuple, suunta: str) -> tuple:
    if suunta == "R":
        return (piste[0], piste[1] + 1)
    elif suunta == "L":
        return (piste[0], piste[1] - 1)
    elif suunta == "D":
        return (piste[0] + 1, piste[1])
    elif suunta == "U":
        return (piste[0] - 1, piste[1])
    else:
        raise ValueError("Väärä suunta paikka_suunnassa:n parametrina")

def sallittu(oma: tuple, suunta: str, kartta: list, kaydyt: list) -> bool:
    oma_kirjain = kirjain_ruudussa(oma, kartta)
    uusi = paikka_suunnassa(oma, suunta)
    if uusi in kaydyt:
        return False
    if uusi[0] < 0 or uusi[1] < 0:
        return False
    if uusi[0] >= len(kartta):
        return False
    if uusi[1] >= len(kartta[uusi[0]]):
        return False
    uusi_kirjain = kirjain_ruudussa(uusi, kartta)
    if oma_kirjain == "S":
        oma_kirjain = "a"
    if uusi_kirjain == "E":
        uusi_kirjain = "z"
    if string.ascii_lowercase.find(uusi_kirjain) == string.ascii_lowercase.find(oma_kirjain) + 1 \
        or string.ascii_lowercase.find(uusi_kirjain) == string.ascii_lowercase.find(oma_kirjain):
        return True
    else:
        return False

def piirra(kartta:list, kaydyt:list):
    piirtokartta = copy.deepcopy(kartta)
    for koordinaatit in kaydyt:
        piirtokartta[koordinaatit[0]][koordinaatit[1]] = "█"
    naytettava = ""
    for rivi in piirtokartta:
        for kirjain in rivi:
            naytettava += kirjain
        naytettava += "\n"
    print("\n"*50)
    print(naytettava)
    time.sleep(0.0005)

def piirra_oma(kartta:list, oma: tuple):
    piirtokartta = copy.deepcopy(kartta)
    piirtokartta[oma[0]][oma[1]] = "🍕"
    naytettava = ""
    for rivi in piirtokartta:
        for kirjain in rivi:
            naytettava += kirjain
        naytettava += "\n"
    os.system("cls")
    print(naytettava)
    time.sleep(0,4)

def astu(oma: tuple, maali: tuple, kartta: list, kaydyt: list) -> tuple:
    piirra(kartta, kaydyt)
    if oma == maali:
        print(f"Perillä swag. Askeleita meni {len(kaydyt)}")
        return (True, len(kaydyt))
    # matka = ekasta_tokaan(oma, maali)
    # navigointi = menosuunnat(matka)
    for suunta in "RUDL":
        seuraava = paikka_suunnassa(oma, suunta)
        if sallittu(oma, suunta, kartta, kaydyt):
            # print(f"Joo astutaan ruutuun {seuraava}, ollaan käyty jo {len(kaydyt)} ruudussa")
            # print(f"Alku löytyy ruudusta {alun_koordinaatit(kartta)}")
            astu(seuraava, maali, kartta, kaydyt + [oma])





with open("data.txt") as f:
    kartta = [[*r.strip()] for r in f]
    
alku = alun_koordinaatit(kartta)
maali = maalin_koordinaatit(kartta)

oma = alku
kaydyt = []

astu(oma, maali, kartta, kaydyt + [alku])
print("öööh")


# with open("alku.txt") as f:
#     kartta = []
#     for r in f:
#         kartta.append([*r.strip()])

#     print(kartta)
