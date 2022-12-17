import apu

kartta = apu.lue_data("data")

avoimet = []

matkat_ruudusta = []
for y in range(len(kartta)):
    matkat_ruudusta.append(["" for leveys in range(len(kartta[y]))])

ansat = []
ansa_alueet = apu.ansat(kartta)
for ansa_alue in ansa_alueet:
    for koordinaatit in ansa_alue:
        ansat.append(koordinaatit)

lahto = apu.etsi_kirjain("S", kartta)
maali = apu.etsi_kirjain("E", kartta)
kartta[lahto[0]][lahto[1]] = "a"
kartta[maali[0]][maali[1]] = "z"

matkat_ruudusta[lahto[0]][lahto[1]] = (0, (20, 0))
avoimet, matkat_ruudusta = apu.arvioi(lahto, kartta, avoimet, matkat_ruudusta)
avoimet.sort(key= lambda avoin: matkat_ruudusta[avoin[0]][avoin[1]][0])
lahto = avoimet.pop(0)

while matkat_ruudusta[maali[0]][maali[1]] == "":
    avoimet, matkat_ruudusta = apu.arvioi(lahto, kartta, avoimet, matkat_ruudusta)
    avoimet.sort(key= lambda avoin: matkat_ruudusta[avoin[0]][avoin[1]][0])
    lahto = avoimet.pop(0)
    
print(matkat_ruudusta[maali[0]][maali[1]])