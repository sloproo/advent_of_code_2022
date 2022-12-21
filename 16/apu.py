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