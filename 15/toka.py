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
            uudet_haarukat.append((alku, loppu))
            alku = haarukat[i][0]
            loppu = haarukat[i][1]
            if i + 1 == len(haarukat):
                uudet_haarukat.append((alku, loppu))

    if uudet_haarukat == haarukat:
        return haarukat
    else:
        return yhdistele(uudet_haarukat)

def rivin_nakyvat_vaakaruudut(rivi: int, sensorit: list) -> int:
    nakyvat_vaakaruudut = [sensorin_haarukka_vaakarivillä(sensori, rivi) for sensori in sensorit]

    haarukat = [haarukka for haarukka in nakyvat_vaakaruudut if haarukka != (0, 0)]

    haarukat = sorted(haarukat, key= lambda haarukka: haarukka[0])

    # Yhdistellään haarukat
    yhdistellyt = yhdistele(haarukat)
    return yhdistellyt

sensorit, majakat = lue("data.txt")
maksimi = 4000000

for y in range(maksimi +1):
    if y % 50000 == 0:
        print(f"Ollaan rivillä {y}")
    peitto = rivin_nakyvat_vaakaruudut(y, sensorit)
    if len(peitto) == 1:
        if 0 < peitto[0][0]:
            print(f"Rivillä {y} peitto oli {peitto} ja ainakin 0 on katveessa.")
            x = 0
            oikea_y = y
            break
        elif maksimi >= peitto[0][1]:
            print(f"Rivillä {y} peitto oli {peitto} ja ainakin {maksimi} on katveessa.")
            x = maksimi
            oikea_y = y
            break
        continue
    elif len(peitto) > 1:
        print(f"Rako peitossa {peitto} rivillä {y}!")
        print(f"Rakoon jäi {peitto[0][1]}")
        x = peitto[0][1]
        oikea_y = y
        break
    else:
        raise ValueError("Rivillä ei lainkaan peittoa")
    

print(f"Sokea piste löytyi kohdasta y = {oikea_y} , x = {x} .")
print(f"Viritystaajuus on {x} * 4000000 + {oikea_y} = {x * 4000000 + oikea_y}")
