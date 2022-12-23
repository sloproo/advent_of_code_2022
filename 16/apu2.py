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

def kierros(ihte: tuple, norsu: tuple, vakiot: tuple, kaydyt: list, avatut: list, aikaa: int,
            paine: int) -> int:
    # print(f"Uusi kierros, aikaa jäljellä: {aikaa}")
    if aikaa == 0:
        # print("Aika loppui, palautetaan")
        return paine
    venttiilit = vakiot[0]
    huoneet = vakiot[1]
    kartoitus = vakiot[2]
    paineen_lisays = 0
    taydennetty_kaydyt = kaydyt.copy()
    taydennetty_avatut = avatut.copy()
    ihte_liikkuu = False
    norsu_liikkuu = False
    paineet_alhaalta = []

    if ihte[0] in venttiilit.keys() and ihte[0] not in avatut and ihte[1] == 0:
        paineen_lisays += (aikaa - 1) * venttiilit[ihte[0]].paine
        taydennetty_avatut.append(ihte[0])
        ihte = (ihte[0], 1)
    if norsu[0] in venttiilit.keys() and norsu[0] not in avatut and norsu[1] == 0:
        paineen_lisays += (aikaa - 1) * venttiilit[norsu[0]].paine
        taydennetty_avatut.append(norsu[0])
        norsu = (norsu[0], 1)
    
    if ihte[1] == 0 and ihte[0] in taydennetty_avatut: ihte_liikkuu = True
    if norsu[1] == 0 and norsu[0] in taydennetty_avatut: norsu_liikkuu = True
    
    if ihte_liikkuu and norsu_liikkuu:
        for oma_seuraava in [tarjokas for tarjokas in venttiilit.keys() if
        tarjokas not in taydennetty_kaydyt and kartoitus[ihte[0]][tarjokas] < aikaa]:
            for norsun_seuraava in [tarjokas for tarjokas in venttiilit.keys() if
            tarjokas not in taydennetty_kaydyt and tarjokas != oma_seuraava and 
            kartoitus[norsu[0]][tarjokas] < aikaa]:
                paine_alhaalta = kierros((oma_seuraava, kartoitus[ihte[0]][oma_seuraava] -1),
                (norsun_seuraava, kartoitus[norsu[0]][norsun_seuraava] -1),
                vakiot,
                taydennetty_kaydyt + [oma_seuraava] + [norsun_seuraava],
                taydennetty_avatut, aikaa -1, paine + paineen_lisays)
                if paine_alhaalta not in paineet_alhaalta:
                    paineet_alhaalta.append(paine_alhaalta)
    elif ihte_liikkuu:
        for oma_seuraava in [tarjokas for tarjokas in venttiilit.keys() if
        tarjokas not in taydennetty_kaydyt and kartoitus[ihte[0]][tarjokas] < aikaa]:
            paine_alhaalta = kierros((oma_seuraava, kartoitus[ihte[0]][oma_seuraava] -1),
            (norsu[0], norsu[1] -1), vakiot,
            taydennetty_kaydyt + [oma_seuraava], taydennetty_avatut, 
            aikaa -1, paine + paineen_lisays)
            if paine_alhaalta not in paineet_alhaalta:
                paineet_alhaalta.append(paine_alhaalta)
    elif norsu_liikkuu:
        for norsun_seuraava in [tarjokas for tarjokas in venttiilit.keys() if
        tarjokas not in taydennetty_kaydyt and kartoitus[norsu[0]][tarjokas] < aikaa]:
            paine_alhaalta = kierros((ihte[0], ihte[1] -1),
            (norsun_seuraava, kartoitus[norsu[0]][norsun_seuraava] -1),
            vakiot, 
            taydennetty_kaydyt + [norsun_seuraava], taydennetty_avatut, 
            aikaa -1, paine + paineen_lisays)
            if paine_alhaalta not in paineet_alhaalta:
                paineet_alhaalta.append(paine_alhaalta)
    elif ihte[1] > 0 or norsu[1] > 0:
        paine_alhaalta = kierros((ihte[0], max([ihte[1]-1, 0])), (norsu[0], max(norsu[1]-1, 0)),
        vakiot, taydennetty_kaydyt, taydennetty_avatut,
        aikaa -1, paine + paineen_lisays)
        if paine_alhaalta not in paineet_alhaalta:
            paineet_alhaalta.append(paine_alhaalta)
    elif [tarjokas for tarjokas in venttiilit.keys() if tarjokas not in taydennetty_kaydyt] == []:
        print(f"Kaikissa huoneissa käyty, aikaa olisi jäänyt vielä {aikaa} minuuttia")
        return paine + paineen_lisays
    elif [tarjokas for tarjokas in venttiilit.keys() if kartoitus[ihte[0]][tarjokas] < aikaa] == [] or [tarjokas for tarjokas in venttiilit.keys() if kartoitus[norsu[0]][tarjokas] < aikaa] == []:
        if [tarjokas for tarjokas in venttiilit.keys() if kartoitus[ihte[0]][tarjokas] < aikaa] == []:
            print("Paikkoja on käymättä mutta ihte ei ehdi.")
        if [tarjokas for tarjokas in venttiilit.keys() if kartoitus[norsu[0]][tarjokas] < aikaa] == []:
            print("Paikkoja on käymättä mutta norsu ei ehdi.")
        paine_alhaalta = kierros((ihte[0], max([ihte[1]-1, 0])), (norsu[0], max(norsu[1]-1, 0)),
        vakiot, taydennetty_kaydyt, taydennetty_avatut,
        aikaa -1, paine + paineen_lisays)
        if paine_alhaalta not in paineet_alhaalta:
            paineet_alhaalta.append(paine_alhaalta)
    else:
        raise ValueError("Kukaan ei liiku tai työskentele, kaikkialla ei ole käyty ja jonnekin ehtisi mutta mitään ei tapahdu. Ongelma!")
    
    if paineet_alhaalta == []:
        # print(f"Palautetaan pohjalta {paine + paineen_lisays}")
        return paine + paineen_lisays
    else:
        # print(f"Palautetaan ylöspäin {max(paineet_alhaalta)}")
        return max(paineet_alhaalta)
    