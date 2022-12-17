import string, copy, math, os, apu
global ratkaisun_askeleita

kartta = apu.lue_data("data")

avoimet = []
matkat = []
poltetut = []
for y in range(len(kartta)):
    matkat.append(["" for leveys in range(len(kartta[y]))])




ansa_alueet = apu.ansat(kartt)
for ansa_alue in ansa_alueet:
    for koordinaatit in ansa_alue:
        poltetut.append(koordinaatit)

lahto = apu.etsi_kirjain("S", kartta)
maali = apu.etsi_kirjain("E", kartta)
kartta[lahto[0]][lahto[1]] = "a"
kartta[maali[0]][maali[1]] = "z"


apu.nayta_tilanne(lahto, kartta, poltetut)

oma = lahto
matkat[oma[0]][oma[1]] = (0, "")

kierros = 0 
while True:
    kierros += 1
    if kierros % 2000 == 0:
        pass
    print(f"Kierros {kierros}")
    avoimet, matkat = apu.arvioi(oma, kartta, avoimet, matkat)
    avoimet.sort(key= lambda avoin: matkat[avoin[0]][avoin[1]][0])
    oma = avoimet.pop(0)
    if matkat[maali[0]][maali[1]] != "":
        print(matkat[maali[0]][maali[1]])
        break
