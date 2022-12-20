def lue(tiedosto: str) -> tuple[list, list]:
    with open(tiedosto) as f:
        sensorit = []
        majakat = []
        for r in f:
            r = r.strip().replace(",", "").split(" ")
            x_sensori = int(r[2][2:])
            y_sensori = int(r[3][2:-1])
            x_majakka = int(r[8][2:])
            y_majakka = int(r[9][2:])
            sade = etaisyys((x_sensori, y_sensori), (x_majakka, y_majakka))
            sensorit.append(((x_sensori, y_sensori), sade))
            majakat.append((x_majakka, y_majakka))
        majakat = list(set(majakat))
        return sensorit, majakat

def etaisyys(eka: tuple, toka: tuple) -> int:
    x1, y1 = eka
    x2, y2 = toka
    return abs(x2 - x1) + abs(y2 - y1)

def sensorin_haarukka_vaakarivillä(sensori: tuple, rivin_y: int) -> tuple[int, int]:
    x, y, sade = sensori[0][0], sensori[0][1], sensori[1]
    if rivin_y < y - sade:
        return (0, 0)
    elif rivin_y > y + sade:
        return (0, 0)
    else:
        return (x - (sade - abs(y - rivin_y)), x + (sade - abs(y - rivin_y)) + 1)

def yhdistele(haarukat: list) -> list:
    haarukat = sorted(haarukat, key= lambda haarukka: haarukka[0])
    if len(haarukat) == 1:
        return haarukat
    uudet_haarukat = []
    alku = haarukat[0][0]
    loppu = haarukat[0][1]
    for i in range(1, len(haarukat)):
        if loppu > haarukat[i][0]:
            loppu = max(loppu, haarukat[i][1])
            if i + 1 == len(haarukat):
                uudet_haarukat.append((alku, loppu))
        else:
            uudet_haarukat.append(alku, loppu)
            alku = haarukat[i][0]
            loppu = haarukat[i][1]
    
    if uudet_haarukat == haarukat:
        return haarukat
    else:
        return yhdistele(uudet_haarukat)

def rivin_nakyvat_vaakaruudut(rivi: int, sensorit: list) -> int:
    nakyvat_vaakaruudut = [sensorin_haarukka_vaakarivillä(sensori, rivi) for sensori in sensorit]

    # Ylempi teki tämän turhaksi. Uskoakseni
    # nakyvat_vaakaruudut = []
    # for sensori in sensorit:
    #     alku, loppu = sensorin_haarukka_vaakarivillä(sensori, tarkkailurivi)
    #     nakyvat_vaakaruudut.append((alku, loppu))
    #     print("Sensori käsitelty")

    haarukat = [haarukka for haarukka in nakyvat_vaakaruudut if haarukka != (0, 0)]

    haarukat = sorted(haarukat, key= lambda haarukka: haarukka[0])

    # Yhdistellään haarukat
    yhdistellyt = yhdistele(haarukat)
    return yhdistellyt


def nakyvien_maara_haarukassa(rivi: list, haarukat: list, majakat: list) -> int:
    nakyvia = 0
    for haarukka in haarukat:
        nakyvia += len(range(haarukka[0], haarukka[1]))

    # Vähennetään mahdolliset majakat tarkasteluriviltä
    for majakka in majakat:
        if majakka[1] == tarkkailurivi:
            for haarukka in haarukat:
                if majakka[0] in range(haarukka[0], haarukka[1]):
                    nakyvia -= 1
    
    return nakyvia

sensorit, majakat = lue("data.txt")
tarkkailurivi = 2000000
haarukat = rivin_nakyvat_vaakaruudut(tarkkailurivi, sensorit)
nakyvia = nakyvien_maara_haarukassa(tarkkailurivi, haarukat, majakat)

print(f"Rivillä {tarkkailurivi} oli {nakyvia} ruutua joissa ei voi olla majakkaa")





# Turhaa roskaa massiivisen karttamatriisin ajatuksesta
# def koordinaatit_kartalle(koordinaatit: tuple, vasen: int, yla: int) -> tuple[int, int]:
#     x, y = koordinaatit
#     x = x - vasen
#     y = y - yla
#     return x, y
        

# vasen_laita = min([s[0][0] - s[1] for s in sensorit])
# oikea_laita = max([s[0][0] + s[1] for s in sensorit])
# ylalaita = min([s[0][1] - s[1] for s in sensorit])
# alalaita = max([s[0][1] + s[1] for s in sensorit])

# kartan_korkeus = alalaita - ylalaita
# kartan_leveys = oikea_laita - vasen_laita
# print(f"Korkeus = {kartan_korkeus}")
# print(f"Leveys: {kartan_leveys}")

