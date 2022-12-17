import string, os, copy

def ruudun_korkeus(koordinaatit: tuple, kartta: list) -> int:
    y, x = koordinaatit
    return kirjaimen_arvo(kartta[y][x])
    

def kirjaimen_arvo(kirjain: str) -> int:
    return string.ascii_lowercase.index(kirjain)

def kirjain_ruudussa(koordinaatit: tuple, kartta:list) -> str:
    return kartta[koordinaatit[0]][koordinaatit[1]]

def rajoissa(koordinaatit: tuple, kartta: list) -> bool:
    y, x = koordinaatit
    if y < 0 or y >= len(kartta):
        return False
    elif x < 0 or x >= len(kartta[y]):
        return False
    else:
        return True

def nousu_mahdollinen(alku: tuple, loppu: tuple, kartta: list) -> bool:
    if ruudun_korkeus(alku, kartta) + 1 >= ruudun_korkeus(loppu, kartta):
        return True
    else:
        return False

def mahdollinen_siirto(alku: tuple, loppu: tuple, kartta: list, kielletyt: list, kaydyt: list) -> bool:
    if not rajoissa(loppu, kartta):
        return False
    elif not nousu_mahdollinen(alku, loppu, kartta):
        return False
    elif loppu in kielletyt:
        return False
    elif loppu in kaydyt:
        return False
    else:
        return True

def ruudun_naapurit(koordinaatit: tuple, kartta: list) -> list:
    palautettavat = []
    for ruutu in [(koordinaatit[0]+1, koordinaatit[1]), (koordinaatit[0]-1, koordinaatit[1]),
                    (koordinaatit[0], koordinaatit[1]+1), (koordinaatit[0], koordinaatit[1]-1)]:
        if rajoissa(ruutu, kartta):
            palautettavat.append(ruutu)
    return palautettavat


def alue_ruudusta(koordinaatit: tuple, kartta: list) -> list:
    alue = [koordinaatit]
    kirjain = kirjain_ruudussa(koordinaatit, kartta)
    while True:
        vanha_pituus = len(alue)
        for vanhan_koordinaatit in alue:
            for naapuri in ruudun_naapurit(vanhan_koordinaatit, kartta):
                if naapuri in alue:
                    continue
                elif kirjain_ruudussa(naapuri, kartta) != kirjain:
                    continue
                else:
                    alue.append(naapuri)
        if vanha_pituus == len(alue):
            break
    return alue

def alueen_kirjaimet(alue: list, kartta: list) -> list:
    palautettavat_kirjaimet = []
    for koordinaatit in alue:
        if kirjain_ruudussa(koordinaatit, kartta) not in palautettavat_kirjaimet:
            palautettavat_kirjaimet.append(kirjain_ruudussa(koordinaatit, kartta))
    return palautettavat_kirjaimet

def alueen_naapurit(alue: list, kartta: list) -> list:
    palautettavat_naapurit = []
    for koordinaatit in alue:
        for naapuri in ruudun_naapurit(koordinaatit, kartta):
            if naapuri in alue:
                continue
            elif naapuri not in palautettavat_naapurit:
                palautettavat_naapurit.append(naapuri)
    return palautettavat_naapurit

def ruutujen_etaisyys(eka: tuple, toka: tuple) -> int:
    return abs(toka[0] - eka[0]) + abs(toka[1] - eka[1])

def luo_alueet(kartta: list) -> list:
    palautettavat_alueet = []
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            for alue in palautettavat_alueet:
                if (y, x) in alue:
                    break
            else:
                palautettavat_alueet.append(alue_ruudusta((y, x), kartta))
    return palautettavat_alueet

def ansa(alue: list, kartta: list) -> bool:
    omat_kirjaimet = alueen_kirjaimet(alue, kartta)
    if len(omat_kirjaimet) != 1:
        raise ValueError("Seka-alue ansoja etsittäessä")
    naapurien_kirjaimet = alueen_kirjaimet(alueen_naapurit(alue, kartta), kartta)
    oma_kirjain = omat_kirjaimet[0]
    for naapurin_kirjain in naapurien_kirjaimet:
        if kirjaimen_arvo(naapurin_kirjain) <= kirjaimen_arvo(oma_kirjain) + 1:
            return False
    else:
        # print(f"Löytyi ansa {alue}")
        return True

def ansat(kartta: list) -> list:
    ansa_alueet = []
    for alue in luo_alueet(kartta):
        if ansa(alue, kartta):
            ansa_alueet.append(alue)
    return ansa_alueet

def alueiden_ruudut(alueet: list) -> list:
    palautettavat_ruudut = []
    for alue in alueet:
        for ruutu in alue:
            palautettavat_ruudut.append(ruutu)
    return palautettavat_ruudut

def etsi_kirjain(kirjain: str, kartta: list) -> tuple:
    for rivi in range(len(kartta)):
        for sarake in range(len(kartta[rivi])):
            if kartta[rivi][sarake] == kirjain:
                return (rivi, sarake)
    else:
        raise ValueError("Ei löytynyt kirjainta")

def nayta_kartta(kartta: list):
    tulostettava = ""
    for rivi in kartta:
        tulostusrivi = "".join(rivi)
        tulostettava += tulostusrivi + "\n"
    print("\n" * 40)
    print(tulostettava)

def nayta_tilanne(kartta: list, kielletyt: list):
    tulostuskartta = copy.deepcopy(kartta)
    for kielletty in kielletyt:
        tulostuskartta[kielletty[0]][kielletty[1]] = " "
    tulostettava = ""
    for rivi in tulostuskartta:
        tulostusrivi = "".join(rivi)
        tulostettava += tulostusrivi + "\n"
    os.system("cls")
    print(tulostettava)

def jarjesta_avoimet(avoimet: list) -> list:
    return sorted(avoimet, key= lambda avoin: avoin[1])

def katsele(sijainti: tuple, kartta: list, jaljet: list, kaydyt: list, kielletyt: list, avoimet: list) -> list:
    liikkeita_takana = jaljet[sijainti[0]][sijainti[1]][0]
    for naapuri in ruudun_naapurit(sijainti, kartta):
        if mahdollinen_siirto(sijainti, naapuri, kartta, kielletyt, kaydyt):
            if not naapuri in [avoin[0] for avoin in avoimet]:
                avoimet.append((naapuri, liikkeita_takana + 1, sijainti))
    avoimet = jarjesta_avoimet(avoimet)
    return avoimet

def liiku(alku: tuple, loppu: tuple, kartta: list, jaljet: list, kaydyt: list, avoimet: list) -> tuple[tuple, list]:
    kaydyt.append(alku)
    matkaa_asken_takana = jaljet[alku[0]][alku[1]][0]
    jaljet[loppu[0]][loppu[1]]  = (matkaa_asken_takana + 1, alku)
    return (loppu, jaljet)

def etsi_kirjaimet(kirjain: str, kartta: list) -> list:
    paikat = []
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            if kartta[y][x] == kirjain:
                paikat.append((y, x))
    return paikat
