def yhdista(eka: tuple, toka: tuple, kartta: list) -> list:
    kivipisteet = []
    if eka[0] == toka[0]:
        x = eka[0]
        for y in range(min(eka[1], toka[1]), max(eka[1], toka[1]) +1):
            kivipisteet.append((x, y))
    elif eka[1] == toka[1]:
        y = eka[1]
        for x in range(min(eka[0], toka[0]), max(eka[0], toka[0]) +1):
            kivipisteet.append((x, y))
    else:
        raise ValueError("Viiva samassa kohdassa olevasta pisteestä itseensä")

    for x, y in kivipisteet:
        kartta[y][x] = "#"
    return kartta

def nayta(kartta:list):
    kokonaisuus = ""
    for rivi in kartta:
        tulostusrivi = ""
        for kohta in rivi:
            tulostusrivi += kohta
        tulostusrivi += "\n"
        kokonaisuus += tulostusrivi
    print(kokonaisuus)

# x- koordinaatti: x - pienin_x + 1
def pudota(koordinaatti: tuple, kartta: list) -> list:
    x, y = koordinaatti
    while kartta[y+1][x] == ".":
        y += 1
    if not kartta[y+1][x] in ["#", "o"]:
        raise ValueError("Nyt pudottiin oudon päälle")
    if kartta[y+1][x-1] == ".":
        kartta = pudota((x-1, y+1), kartta)
    elif kartta[y+1][x+1] == ".":
        kartta = pudota((x+1, y+1), kartta)
    else:
        kartta[y][x] = "o"
    return kartta

viivat = []
with open("data.txt") as f:
    for r in f:
        viivat.append([tuple(int(numero) for numero in piste.split(",")) for piste in r.strip().split(" -> ")])
        pass

kaikki_pisteet = set(piste for viiva in viivat for piste in viiva)
vaaka = sorted(kaikki_pisteet, key= lambda piste: piste[0])
pysty = sorted(kaikki_pisteet, key= lambda piste: piste[1])
pienin_x = vaaka[0][0]  
suurin_x = vaaka[-1][0]
pienin_y = pysty[0][1]
suurin_y = pysty[-1][1]

leveys = 1000
korkeus = suurin_y

kartta = []
for i in range(korkeus+2):
    kartta.append(["." for __ in range(leveys + 2)])
kartta.append(["#" for __ in range(leveys + 2)])

for viiva in viivat:
    for p in range(1, len(viiva)):
        eka = viiva[p-1]
        toka = viiva[p]
        kartta = yhdista(eka, toka, kartta)


i = 0
try:
    while True:
        i += 1
        # print(f"pudotetaan {i}. hiekanjyvänen")
        kartta = pudota((500, 0), kartta)
        # print(f"pudotettiin {i}. hiekanjyvänen")
        if kartta[0][500] == "o":
            print(f"{i} hiekanjyvästä pudotettiin, vikan jälkeen tuloreikä on tukossa")
            break

except IndexError:
    nayta(kartta)
    print(f"Pudotettiin onnistuneesti {i-1} hiekanjyvästä")