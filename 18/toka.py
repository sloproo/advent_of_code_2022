def naapurit(x: int, y: int, z: int) -> list:
    palautettavat = []
    palautettavat.append((x+1, y, z))
    palautettavat.append((x-1, y, z))
    palautettavat.append((x, y+1, z))
    palautettavat.append((x, y-1, z))
    palautettavat.append((x, y, z+1))
    palautettavat.append((x, y, z-1))
    return palautettavat

vokselit = []
vapaita_sivuja = 0

min_x = ""
with open("data.txt") as f:
    for r in f:
        x, y, z = (int(luku)+1 for luku in r.strip().split(","))
        if min_x == "":
            min_x = x
            max_x = x
            min_y = y
            max_y = y
            min_z = z
            max_z = z
        else:
            min_x = min((min_x, x))
            min_y = min((min_y, y))
            min_z = min((min_z, z))
            max_x = max((max_x, x))
            max_y = max((max_y, y))
            max_z = max((max_z, z))
        viereiset = naapurit(x, y, z)
        sivuja_tulossa = 6
        for naapuri in viereiset:
            if naapuri in vokselit:
                sivuja_tulossa -= 1
        vapaita_sivuja = vapaita_sivuja - 6 + (2 * sivuja_tulossa)
        vokselit.append((x, y, z))

print(f"Vapaita sivuja on {vapaita_sivuja}")
print(f"max_x: {max_x} , max_y: {max_y} , max_z: {max_z}")

print(f"min_x: {min_x} , min_y: {min_y} , min_z: {min_z}")


kaydyt = []
kaytavat = [(0, 0, 0)]
ulkoilmakontaktia = 0
while True:
    seuraavaksi_kaytavat = []
    lisattavat = []
    for ilmaruutu in kaytavat:
        for naapuri in naapurit(ilmaruutu[0], ilmaruutu[1], ilmaruutu[2]):
            if naapuri in kaydyt or naapuri in kaytavat or naapuri in seuraavaksi_kaytavat:
                continue
            elif -1 in [naapuri[0], naapuri[1], naapuri[2]] or 22 in [naapuri[0],
                naapuri[1], naapuri[2]]:
                if naapuri not in kaydyt:
                    kaydyt.append(naapuri)
                continue
            elif naapuri in vokselit:
                ulkoilmakontaktia += 1
            else:
                if naapuri not in seuraavaksi_kaytavat:
                    seuraavaksi_kaytavat.append(naapuri)
    kaydyt += kaytavat
    if seuraavaksi_kaytavat != []:
        kaytavat = seuraavaksi_kaytavat
        print(ulkoilmakontaktia)
    else:
        break
    # print("ilmaruutu käyty")

print(f"Ulkoilmakontaktia on {ulkoilmakontaktia} taholla")
