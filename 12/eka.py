import apu

with open("data.txt") as f:
    kartta = [[*r.strip()] for r in f]

aloitus = apu.etsi_kirjain("S", kartta)
maali = apu.etsi_kirjain("E", kartta)

kartta[aloitus[0]][aloitus[1]] = "a"
kartta[maali[0]][maali[1]] = "z"

kielletyt = apu.alueiden_ruudut(apu.ansat(kartta))

apu.nayta_tilanne(kartta, kielletyt)

