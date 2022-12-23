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
    # Alla <2 vai <1?
    if aikaa < 1:
        # print(f"Aikaa alle minuutti, palautetaan")
        if kootut_paineet != []:
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























































































def huoneessa(venttiilit: dict, huoneet: dict, kartoitus: dict, kaydyt: list, 
        saavuttu: str, aikaa: int, paine: int) -> tuple[int, list]:
    if len(saavuttu) == 1: raise ValueError("Miten voi saapua tämännimiseen huoneeseen")
    kaydyt.append(saavuttu)
    paineet_alempaa = []
    if aikaa < 1:
        if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
        return paine, kaydyt[:-1]
    if saavuttu in venttiilit.keys():
        paine += (aikaa := aikaa - 1) * venttiilit[saavuttu].paine
    for venttiili in [tarjokas for tarjokas in venttiilit.keys() if tarjokas not in kaydyt]:
        if venttiili in kaydyt:
            continue
        else:
            uusi_kaydyt = [kayty for kayty in kaydyt]
            myohemmasta, kaydyt = huoneessa(venttiilit, huoneet, kartoitus, uusi_kaydyt, 
                venttiili, aikaa - kartoitus[saavuttu][venttiili], paine)
            paineet_alempaa.append(myohemmasta)
            continue
    if aikaa < 1 or len([venttiili for venttiili in venttiilit.keys() if venttiili not in kaydyt]) == 0:
        if paineet_alempaa == []:
            if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
            return paine, kaydyt[:-1]
        else:
            if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
            return max([paine, max(paineet_alempaa)]), kaydyt[:-1]
    else:
        if "paineet_alempaa" in locals() and paineet_alempaa != []:
            if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
            return (max(max(paineet_alempaa)), paine), kaydyt[:-1]
        if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
        return paine, kaydyt[:-1]


# Rajusti kommentoitu versio alla

# def huoneessa(venttiilit: dict, huoneet: dict, kartoitus: dict, kaydyt: list, saavuttu: str, aikaa: int, paine: int) -> int:
#     print(f"Saavutaan huoneeseen {saavuttu}")
#     if len(saavuttu) == 1: raise ValueError("Miten voi saapua tämännimiseen huoneeseen")
#     print(f"Lisätään se käytyjen listaan {kaydyt}")
#     kaydyt.append(saavuttu)
#     print(f"Aikaa on nyt jäljellä {aikaa} , painetta on {paine}")
#     paineet_alempaa = []
#     if aikaa < 1:
#         print(f"Aika loppui saapuessa, palautetaan ylöspäin paine {paine}")
#         if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
#         return paine, kaydyt[:-1]
#     if saavuttu in venttiilit.keys():
#         print(f"Aikaa on ja huoneessa on venttiili")
#         paine += (aikaa := aikaa - 1) * venttiilit[saavuttu].paine
#         print(f"Paineeseen lisätään {aikaa} min * {venttiilit[saavuttu].paine} baria")
#         print(f"Paine on nyt {paine}")
#     print(f"Etsitään seuraava venttiilihuone")
#     print(f"Käydyt = {kaydyt}")
#     for venttiili in [tarjokas for tarjokas in venttiilit.keys() if tarjokas not in kaydyt]:
#         if venttiili in kaydyt:
#             print(f"{venttiili} :ssä on jo käyty")
#             continue
#         else:
#             print(f"{venttiili} : ssä ei ole vielä käyty")
#             print(f"Sinne matkustamiseen menee aikaa {kartoitus[saavuttu][venttiili]} minuuttia")
#             print(f"Kopioidaan käytyjen listasta uusi eteenpäin menoon annettava kopio")
#             uusi_kaydyt = [kayty for kayty in kaydyt]
#             myohemmasta, kaydyt = huoneessa(venttiilit, huoneet, kartoitus, uusi_kaydyt, 
#                 venttiili, aikaa - kartoitus[saavuttu][venttiili], paine)
#             print(f"Reissulta {venttiili} :stä palattiin huoneeseen {saavuttu}")
#             print(f"Sieltä palattiin paineluvun {myohemmasta} kanssa, lisätään se alempaa saatujen listaan")
#             paineet_alempaa.append(myohemmasta)
#             print(f"Käytyjen lista on nyt {kaydyt}")
#             continue
#     if aikaa < 1 or len([venttiili for venttiili in venttiilit.keys() if venttiili not in kaydyt]) == 0:
#         print(f"Aika loppuu ( {aikaa} tai kaikki venttiilit {venttiilit.keys()} ovat käytyjen listassa {kaydyt}")
#         if paineet_alempaa == []:
#             print(f"Syvemmältä saatuja paineita ei ollut, palautetaan ylöspäin {paine}")
#             if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
#             return paine, kaydyt[:-1]
#         else:
#             print(f"Palautetaan nykyisen paineen {paine} tai myöhempien paineiden {paineet_alempaa} maksimi {max(paineet_alempaa)}")
#             if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
#             return max([paine, max(paineet_alempaa)]), kaydyt[:-1]
#     else:
#         print(f"Aikaa on ja kaikkialla ei ole käyty")
#         print(f"{aikaa} , {kaydyt} , {paine}")
#         print(f"Onkohan vanhempia paineita?")
#         if "paineet_alempaa" in locals() and paineet_alempaa != []:
#             print("oli")
#             if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
#             return (max(max(paineet_alempaa), paine)), kaydyt[:-1]
#         print(f"Ei näköjään, palautetaan vaikka sit paine {paine} ja käydyt miinus vika {kaydyt[:-1]}")
#         if len(kaydyt[-1]) == 1: raise ValueError("Täältä nousee ylös liian lyhyt käyty")
#         return paine, kaydyt[:-1]

