import apu

with open("data.txt") as f:
    kartta = [[*r.strip()] for r in f]

aloitus = apu.etsi_kirjain("S", kartta)
maali = apu.etsi_kirjain("E", kartta)

kartta[aloitus[0]][aloitus[1]] = "a"
kartta[maali[0]][maali[1]] = "z"

kielletyt = apu.alueiden_ruudut(apu.ansat(kartta))
kaydyt = [aloitus]

apu.nayta_tilanne(kartta, kielletyt)

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

print(avoimet)


while sijainti != maali:
    avoimet = apu.katsele(sijainti, kartta, jaljet, kaydyt, kielletyt, avoimet)
    seuraava = avoimet.pop(0)
    sijainti, jaljet = apu.liiku(seuraava[2], seuraava[0], kartta, jaljet, kaydyt, avoimet)

print(f"Maaliin päästiin, sijainti == {sijainti}")
print(f"Matkaan meni {jaljet[maali[0]][maali[1]][0]} askelta")
