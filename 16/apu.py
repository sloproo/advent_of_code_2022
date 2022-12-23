def katsele(oma: str, huoneet: dict, avoimet: list, jaljet: list) -> list:
    naapurit = huoneet[oma[0]].reitit
    for naapuri in naapurit:
        for avoin in avoimet:
            if naapuri == avoin[0] and oma[1] + 1 >= avoin[1]:
                break
        else:
            avoimet.append((naapuri, oma[1] + 1))
    avoimet.sort(key= lambda avoin: avoin[1])
    return avoimet

def liiku(loppu: str, kaydyt: list) -> tuple[str, list]:
    kaydyt.append((loppu[0], loppu[1]+1))
    return (loppu, kaydyt)

def dijkstra(alku: str, maali: str, huoneet: dict) -> int:
    oma = (alku, 0)
    avoimet = []
    kaydyt = []
    while oma[0] != maali:
        avoimet = katsele(oma, huoneet, avoimet, kaydyt)
        seuraava = avoimet.pop(0)
        oma, kaydyt = liiku(seuraava, kaydyt)
    return oma[1]

def kartoita(huoneet: dict) -> dict:
    huoneiden_nimet = [huone for huone in huoneet.keys()]
    matkat = {}
    for alku in huoneiden_nimet:
        for maali in huoneiden_nimet:
            if alku == maali: continue
            matka = dijkstra(alku, maali, huoneet)
            if alku not in matkat.keys():
                matkat[alku] = {}
            matkat[alku][maali] = matka
    return matkat

def huoneeseen(venttiilit: dict, huoneet: dict, kartoitus: dict, kaydyt: list, 
        saapumishuone: str, aikaa: int, paine: int) -> int:
    taydennetty_kaydyt = kaydyt + [saapumishuone]
    # print(f"Saavutaan huoneeseen {saapumishuone}")
    # print(f"Käydyt huoneet: {kaydyt}")
    kootut_paineet = []
    if aikaa < 1:
        # print(f"Aikaa alle minuutti, palautetaan")
        if kootut_paineet != []:
            raise ValueError("Tänne ei pitäisi vissiin joutua koskaan")
            return max(paine, max(kootut_paineet))
        else:
            return paine
    if saapumishuone in venttiilit.keys():
        # print(f"Avataan venttiili")
        paineen_lisays = (aikaa := aikaa -1) * venttiilit[saapumishuone].paine
        kootut_paineet.append(paine+paineen_lisays)
    else:
        paineen_lisays = 0
    for venttiilihuone in [tarjokas for tarjokas in venttiilit.keys() if tarjokas not in taydennetty_kaydyt]:
        # Tätä alemmalla rivillä: uusi_käydyt vai pelkkä käydyt? Sotkeeko kun käytyjä yllä iteroidaan?
        # print(f"Mennään huoneeseen {venttiilihuone}")
        # print(f"Aikaa menee {kartoitus[saapumishuone][venttiilihuone]}")
        # print(f"Aikaa jäljellä {aikaa - kartoitus[saapumishuone][venttiilihuone]}")
        alempaa_saatu = huoneeseen(venttiilit, huoneet, kartoitus, taydennetty_kaydyt,
                        venttiilihuone, aikaa - kartoitus[saapumishuone][venttiilihuone], 
                        paine + paineen_lisays)
        if alempaa_saatu == 1660:
            print(kaydyt)
        kootut_paineet.append(alempaa_saatu)
        continue
    # print(f"Kaikki vaihtoehdot läpikäyty, palautetaan ylöspäin max {paine} vs.")
    # print(f"max {paineet_alempaa}")
    kootut_paineet = list(set(kootut_paineet))
    pass

    return max(kootut_paineet)
