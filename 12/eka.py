import string, time, copy, math, os

def lue_data(tiedosto: str) -> list:
    with open(tiedosto + ".txt") as f:
        return [[*r.strip()] for r in f]

def kirjain_ruudussa(koordinaatit: tuple, kartta: list) -> str:
    return kartta[koordinaatit[0]][koordinaatit[1]]

def etsi_kirjain(kirjain: str, kartta: list) -> tuple:
    for rivi in range(len(kartta)):
        for sarake in range(len(kartta[rivi])):
            if kartta[rivi][sarake] == kirjain:
                return (rivi, sarake)
    else:
        raise ValueError("Ei löytynyt kirjainta")

def ruudukossa(koordinaatit: tuple, kartta: list) -> bool:
    if koordinaatit[0] < 0 or koordinaatit[1] < 0:
        return False
    if koordinaatit[0] >= len(kartta):
        return False
    if koordinaatit[1] >= len(kartta[koordinaatit[0]]):
        return False
    else:
        return True

def kirjaimen_arvo(kirjain: str) -> int:
    return string.ascii_lowercase.find(kirjain)

def sallittu_liike(eka_ruutu: tuple, toka_ruutu: tuple, kartta: list) -> bool:
    if not ruudukossa(toka_ruutu, kartta):
        return False
    eka_kirjain = kirjain_ruudussa(eka_ruutu, kartta)
    toka_kirjain = kirjain_ruudussa(toka_ruutu, kartta)
    if eka_kirjain == "S":
        ekan_arvo = kirjaimen_arvo("a")
    else: 
        ekan_arvo = kirjaimen_arvo(eka_kirjain)
    if toka_kirjain == "E":
        tokan_arvo = kirjaimen_arvo("z")
    else:
        tokan_arvo = kirjaimen_arvo(toka_kirjain)
    if tokan_arvo < ekan_arvo:
        return False
    if ekan_arvo + 1 >= tokan_arvo:
        return True
    else:
        return False

def liikkeen_ruutu(alku: tuple, suunta: str, kartta: list) -> tuple:
    if suunta not in "RUDL":
        raise KeyError("Kelvoton suunta")
    elif suunta == "D":
        palautettava = (alku[0]+1, alku[1])
    elif suunta == "U":
        palautettava = (alku[0]-1, alku[1])
    elif suunta == "R":
        palautettava = (alku[0], alku[1]+1)
    elif suunta == "L":
        palautettava = (alku[0], alku[1]-1)
    # if not ruudukossa(palautettava, kartta):
    #     raise KeyError("Kelvoton suunta")
    return palautettava

def nayta(ruutu: tuple, kartta: list, kaytetyt: list):
    tulostuskartta = copy.deepcopy(kartta)
    for kaytetty in kaytetyt:
        tulostuskartta[kaytetty[0]][kaytetty[1]] = "█"
    tulostuskartta[ruutu[0]][ruutu[1]] = "▄"
    tulostettava = ""
    for rivi in tulostuskartta:
        tulostusrivi = "".join(rivi)
        tulostettava += tulostusrivi + "\n"
    os.system("cls")
    print(tulostettava)

def etaisyys_pisteesta(eka: tuple, toka: tuple) -> float:
    return math.sqrt((toka[1]-eka[1])** 2 + (toka[0]-eka[0])** 2)

def priorisoidut_suunnat(alku: tuple, maali: tuple) -> str:
    suunnat = [(suunta, liikkeen_ruutu(alku, suunta, kartta)) for suunta in "RUDL"]
    jarjestetyt = sorted(suunnat, key=lambda suunta: etaisyys_pisteesta(suunta[1], maali))
    return jarjestetyt


def liiku(alku: tuple, maali: tuple, kartta: list, kaytetyt: list) -> tuple:
    nayta(alku, kartta, kaytetyt)
    if alku == maali:
        print(f"Swag swag maalissa. Askeleita meni {len(kaytetyt)}")
    suunnat = priorisoidut_suunnat(alku, maali)
    for suunta in suunnat:
        uusi_ruutu = liikkeen_ruutu(alku, suunta[0], kartta)
        if uusi_ruutu in kaytetyt or not ruudukossa(uusi_ruutu, kartta):
            continue
        elif sallittu_liike(alku, uusi_ruutu, kartta):
            # print(f"Liikutaan ruudusta {alku} ruutuun {uusi_ruutu}")
            liiku(uusi_ruutu, maali, kartta, kaytetyt + [alku])





kartta = lue_data("data")
alku = etsi_kirjain("S", kartta)
maali = etsi_kirjain("E", kartta)
liiku(alku, maali, kartta, [] + [alku])

