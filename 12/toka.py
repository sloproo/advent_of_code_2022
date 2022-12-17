import apu

with open("data.txt") as f:
    kartta = [[*r.strip()] for r in f]

aloitus = apu.etsi_kirjain("S", kartta)
maali = apu.etsi_kirjain("E", kartta)

kartta[aloitus[0]][aloitus[1]] = "a"
kartta[maali[0]][maali[1]] = "z"

kielletyt = apu.alueiden_ruudut(apu.ansat(kartta))

a_kirjaimet = apu.etsi_kirjaimet("a", kartta)
for ruutu in kielletyt:
    if ruutu in a_kirjaimet:
        a_kirjaimet.remove(ruutu)

apu.nayta_tilanne(kartta, kielletyt)


matkojen_pituudet = []

for a_koordinaatit in a_kirjaimet:
    aloitus = a_koordinaatit
    kaydyt = [aloitus]
    jaljet = []
    for y in range(len(kartta)):
        jaljet.append(["" for _ in range(len(kartta[y]))])
    jaljet[aloitus[0]][aloitus[1]] = (0, (0, 0))

    sijainti = aloitus
    liikkeita_tehty = 0
    avoimet = []
    for naapuri in apu.ruudun_naapurit(aloitus, kartta):
        if apu.mahdollinen_siirto(sijainti, naapuri, kartta, kielletyt, kaydyt):
            avoimet.append((naapuri, liikkeita_tehty + 1, sijainti))

    while sijainti != maali:
        avoimet = apu.katsele(sijainti, kartta, jaljet, kaydyt, kielletyt, avoimet)
        seuraava = avoimet.pop(0)
        sijainti, jaljet = apu.liiku(seuraava[2], seuraava[0], kartta, jaljet, kaydyt, avoimet)

    print(f"Kierros {a_kirjaimet.index(a_koordinaatit)+1} / {len(a_kirjaimet)} ratkaistu")
    print(f"Matkaan meni {jaljet[maali[0]][maali[1]][0]} askelta")
    if jaljet[maali[0]][maali[1]][0] not in matkojen_pituudet:
        matkojen_pituudet.append(jaljet[maali[0]][maali[1]][0])

print(f"Kaikki matkat käyty")
print(f"Lyhin matkan pituus oli {min(matkojen_pituudet)}")
