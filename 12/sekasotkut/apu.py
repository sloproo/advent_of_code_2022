import os, copy, string

def lue_data(tiedosto: str) -> list:
    with open(tiedosto + ".txt") as f:
        return [[*r.strip()] for r in f]

def mahdolliset(ruutu: tuple, kartta: list) -> list:
    naapurit = ruudun_naapurit(ruutu, kartta)
    mahdolliset = [naapuri for naapuri in naapurit if nousu_ok(ruutu, naapuri, kartta)]
    return mahdolliset
    
def arvioi(oma: tuple, kartta: list, avoimet: list, matkat: list) -> tuple[list, list]:
    tahanastinen_matka = matkat[oma[0]][oma[1]][0]
    kelpaavat = mahdolliset(oma, kartta)
    for m_y, m_x in kelpaavat:
        if matkat[m_y][m_x] == "":
            matkat[m_y][m_x] = (tahanastinen_matka + 1, oma)
            avoimet.append((m_y, m_x))
        elif matkat[m_y][m_x][0] < tahanastinen_matka + 1:
            matkat[m_y][m_x] = (tahanastinen_matka + 1, oma)
            avoimet.append((m_y, m_x))
    return (avoimet, matkat)

def kirjain_ruudussa(koordinaatit: tuple, kartta: list) -> str:
    return kartta[koordinaatit[0]][koordinaatit[1]]

def ruudun_korkeus(ruutu: tuple, kartta: list) -> int:
    return kirjaimen_arvo(kirjain_ruudussa(ruutu, kartta))

def kirjaimen_arvo(kirjain: str) -> int:
    if kirjain == "S":
        return string.ascii_lowercase.find("a")
    elif kirjain == "E":
        return string.ascii_lowercase.find("z")
    elif kirjain == ".":
        return 
    return string.ascii_lowercase.find(kirjain)

def korkeuden_kirjain(korkeus: int) -> str:
    return string.ascii_lowercase[int]


def etsi_kirjain(kirjain: str, kartta: list) -> tuple:
    for rivi in range(len(kartta)):
        for sarake in range(len(kartta[rivi])):
            if kartta[rivi][sarake] == kirjain:
                return (rivi, sarake)
    else:
        raise ValueError("Ei löytynyt kirjainta")

def kelpaa(koordinaatit: tuple, kartta: list) -> bool:
    if not ruudukossa(koordinaatit, kartta):
        return False
    elif kirjain_ruudussa(koordinaatit, kartta) == " ":
        return False
    
    else:
        return True

def ruudukossa(koordinaatit: tuple, kartta: list) -> bool:
    if koordinaatit[0] < 0 or koordinaatit[1] < 0:
        return False
    if koordinaatit[0] >= len(kartta):
        return False
    if koordinaatit[1] >= len(kartta[koordinaatit[0]]):
        return False
    else:
        return True

def pisteiden_etaisyys(eka: tuple, toka: tuple) -> int:
    return abs(toka[0] - eka[0]) + abs(toka[1] - eka[1])

def nayta_kartta(kartta: list):
    tulostettava = ""
    for rivi in kartta:
        tulostusrivi = "".join(rivi)
        tulostettava += tulostusrivi + "\n"
    print("\n" * 40)
    print(tulostettava)

def nayta_tilanne(oma: tuple, kartta: list, poltetut: list):
    tulostuskartta = copy.deepcopy(kartta)
    for poltettu in poltetut:
        tulostuskartta[poltettu[0]][poltettu[1]] = " "
    tulostuskartta[oma[0]][oma[1]] = "🙂"
    tulostettava = ""
    for rivi in tulostuskartta:
        tulostusrivi = "".join(rivi)
        tulostettava += tulostusrivi + "\n"
    os.system("cls")
    print(tulostettava)

def nayta_kirjaimet_kartalla(kirjaimet: list, kartta: list) -> list:
    tulostuskartta = copy.deepcopy(kartta)
    for y in range(len(tulostuskartta)):
        for x in range(len(tulostuskartta[y])):
            if tulostuskartta[y][x] in kirjaimet:
                pass
            else:
                tulostuskartta[y][x] = " "
    nayta_kartta(tulostuskartta)

def ruudun_naapurit(koordinaatit: tuple, kartta: list) -> list:
    palautettavat = []
    for ruutu in [(koordinaatit[0]+1, koordinaatit[1]), (koordinaatit[0]-1, koordinaatit[1]),
                    (koordinaatit[0], koordinaatit[1]+1), (koordinaatit[0], koordinaatit[1]-1)]:
        if kelpaa(ruutu, kartta):
            palautettavat.append(ruutu)
    # if not ruudukossa(palautettavat, kartta):
    #     raise KeyError("Kelvoton suunta")
    return palautettavat

def nayta_rajapinnat(kartta: list, poltetut: list):
    ruudut_rajapinnalla = []
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            oma_korkeus = ruudun_korkeus((y, x), kartta)
            for naapurin_koordinaatit in ruudun_naapurit((y, x), kartta, poltetut):
                if abs(ruudun_korkeus((y, x), kartta) - ruudun_korkeus(naapurin_koordinaatit, kartta)) == 1:
                    if (y, x) not in ruudut_rajapinnalla:
                        ruudut_rajapinnalla.append((y, x))
                    if naapurin_koordinaatit not in ruudut_rajapinnalla:
                        ruudut_rajapinnalla.append(naapurin_koordinaatit)
    rajapintakartta = copy.deepcopy(kartta)
    for y in range(len(rajapintakartta)):
        for x in range(len(rajapintakartta[y])):
            if (y, x) not in ruudut_rajapinnalla:
                rajapintakartta[y][x] = " "
    nayta_kartta(rajapintakartta)

def rajapinta_kirjaimeen(koordinaatit: tuple, kirjaimeen: str, kartta: list, poltetut: list) -> list:
    oma_alue = alue_ruudusta(koordinaatit, kartta)
    rajapintaruudut = []
    for poltettu in poltetut:
        if poltettu in oma_alue:
            oma_alue.remove(poltettu)
    for ruutu in oma_alue:
        naapurit = ruudun_naapurit(koordinaatit, kartta, poltetut)
        for naapuri in naapurit:
            if kirjain_ruudussa(naapuri) == kirjaimeen:
                rajapintaruudut.append(naapuri)
    return rajapintaruudut



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

def alueen_naapurit(alue: list, kartta: list) -> list:
    palautettavat_naapurit = []
    for koordinaatit in alue:
        for naapuri in ruudun_naapurit(koordinaatit, kartta):
            if naapuri in alue:
                continue
            elif naapuri not in palautettavat_naapurit:
                palautettavat_naapurit.append(naapuri)
    return palautettavat_naapurit

def alueen_kirjaimet(alue: list, kartta: list) -> list:
    palautettavat_kirjaimet = []
    for koordinaatit in alue:
        if kirjain_ruudussa(koordinaatit, kartta) not in palautettavat_kirjaimet:
            palautettavat_kirjaimet.append(kirjain_ruudussa(koordinaatit, kartta))
    return palautettavat_kirjaimet

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

def etenemiskelvoton(alue: list, kartta: list) -> bool:
    omat_kirjaimet = alueen_kirjaimet(alue, kartta)
    if len(omat_kirjaimet) != 1:
        raise ValueError("Ansassa omana alue, jolla on useampaa eri kirjainta")
    naapurien_kirjaimet = alueen_kirjaimet(alueen_naapurit(alue, kartta), kartta)
    oma_kirjain = omat_kirjaimet[0]
    if oma_kirjain == "z":
        return False
    for naapurin_kirjain in naapurien_kirjaimet:
        if kirjaimen_arvo(naapurin_kirjain) == kirjaimen_arvo(oma_kirjain) + 1:
            return False
    else:
        # print(f"Löytyi etenemiskelvoton alue {alue}.")
        return True

def ansat(kartta: list) -> list:
    ansojen_lista = []
    for alue in luo_alueet(kartta):
        if ansa(alue, kartta):
            ansojen_lista.append(alue)
    return ansojen_lista

def etenemiskelvottomat(kartta: list) -> list:
    kelvottomien_lista = []
    for alue in luo_alueet(kartta):
        if etenemiskelvoton(alue, kartta):
            kelvottomien_lista.append(alue)
    return kelvottomien_lista

def suttaa(koordinaatit: tuple, kartta: list) -> list:
    (y, x) = koordinaatit
    kartta[y][x] = "."
    return kartta

def nousu_ok(alku: tuple, loppu:tuple, kartta: list) -> bool:
    if ruudun_korkeus(alku, kartta) + 1 >= ruudun_korkeus(loppu, kartta):
        return True
    else:
        return False

def sallittu_liike(alku: tuple, loppu: tuple, kartta: list, poltetut: list) -> bool:
    if not kelpaa(loppu, kartta, poltetut):
        return False
    if loppu in poltetut:
        return False
    if kirjain_ruudussa(loppu, kartta) == " ":
        return False
    return nousu_ok(alku, loppu, kartta)

def suunnassa_ruutu(alku: tuple, suunta: str, kartta: list) -> tuple:
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
    # Tämä vissiin tulee tarkastettua muualla
    # if not ruudukossa(palautettava, kartta):
    #     raise ValueError(f"Suunta {suunta} koordinaateista {alku} meni ulos koordinaatistosta.")
    return palautettava

def priorisoidut_suunnat(lahto: tuple, maali: tuple, kartta:list) -> str:
    suunnat = [(suunta, suunnassa_ruutu(lahto, suunta, kartta)) for suunta in "RUDL"]
    jarjestetyt = sorted(suunnat, key=lambda suunta: (ruudun_korkeus(suunnassa_ruutu(lahto, suunta[0], kartta), kartta), 
                                                    pisteiden_etaisyys(suunta[1], maali)))
    # jarjestetyt = sorted(suunnat, key=lambda suunta: ruudun_korkeus(suunnassa_ruutu(lahto, suunta[0], kartta), kartta))
    return jarjestetyt

def uudelle_alueelle(vanha: tuple, uusi: tuple, kartta: list, poltetut: list) -> tuple:
    vanhat_ruudut = alue_ruudusta(vanha, kartta)
    for vanha_ruutu in vanhat_ruudut:
        if vanha_ruutu not in poltetut:
            poltetut.append(vanha_ruutu)
    uuden_korkeus = ruudun_korkeus(uusi, kartta)
    alueen_naapurit = alueen_naapurit(alue_ruudusta(uusi, kartta))
    naapurien_korkeudet = []
    for naapuriruutu in alueen_naapurit:
        if ruudun_korkeus(naapuriruutu, kartta) not in naapurien_korkeudet:
            naapurien_korkeudet.append(ruudun_korkeus(naapuriruutu, kartta))
    naapurien_korkeudet = sorted([korkeus for korkeus in naapurien_korkeudet if korkeus <= uuden_korkeus + 1], reverse=True)
    uusi_tavoitekorkeus = naapurien_korkeudet[0]
    tavoiteruudut = rajapinta_kirjaimeen(uusi, korkeuden_kirjain(uusi_tavoitekorkeus),
                                        kartta, poltetut)
    for poltettava in alue_ruudusta(vanha, kartta):
        if poltettava not in poltetut:
            poltetut.append(poltettava)
    return (tavoiteruudut, poltetut)

        



def astutaanko_umpikujaan(saapumisruutu: tuple, kartta: list, kaytetyt: list, lahtoruutu: tuple) -> bool:
    kartta = copy.deepcopy(kartta)
    for koordinaatit in kaytetyt:
        kartta = suttaa(koordinaatit, kartta)
    kartta = suttaa(lahtoruutu, kartta)
    saap_alue = alue_ruudusta(saapumisruutu, kartta)
    if len(alueen_kirjaimet(saap_alue, kartta)) != 1:
        raise ValueError(f"Nyt tuli epätasainen alue umpikujaan astuessa miettiessä ruudussa {saapumisruutu}")
    alueen_kirjain = kirjain_ruudussa(saapumisruutu, kartta)
    alueen_korkeus = kirjaimen_arvo(alueen_kirjain)
    naapuriruudut = alueen_naapurit(saap_alue, kartta)
    kelvottomat_naapurit = []
    for ruutu in naapuriruudut:
        if ruudun_korkeus(ruutu, kartta) != alueen_korkeus + 1:
            kelvottomat_naapurit.append(ruutu)
        else:
            print(f"Ei astuttu umpikujaan astuttaessa {lahtoruutu} -> {saapumisruutu}")
            print(f"Ruutu {ruutu} on korkeudella {ruudun_korkeus(ruutu, kartta)} kun taso jolta noustaan on {alueen_korkeus}")
            return False
    for ruutu in kelvottomat_naapurit:
        naapuriruudut.remove(ruutu)
    if len(naapuriruudut) != 0:
        raise ValueError("Kaikki ruudun_naapurit muka veivät umpikujaan mutta kaikkia ei poistettu")
    print(f"Astuttiin umpikujaan {lahtoruutu} -> {saapumisruutu}")
    return True