import apu2, time, itertools
from apu import huoneeseen
aika_alussa = time.time()

class Huone:
    def __init__(self, nimi: str, paine: int, reitit: list):
        self.nimi = nimi
        self.paine = paine
        self.reitit = reitit
    def __repr__(self) -> str:
        return f"nimi: {self.nimi} , paine: {self.paine} , reitit: {self.reitit}\n"

huoneet = {}
with open("data.txt") as f:
    for r in f:
        sanat = r.strip().split(" ")
        nimi = sanat[1]
        paine = int(sanat[4][5:-1])
        reitit = [sana.replace(",", "") for sana in sanat[9:]]
        huoneet[nimi] = Huone(nimi, paine, reitit)

kartoitus = apu2.kartoita(huoneet)

venttiilit = {huoneet[huone].nimi: huoneet[huone] for huone in huoneet.keys() if huoneet[huone].paine > 0}
# venttiilit = [huoneet[huone] for huone in huoneet.keys() if huoneet[huone].paine > 0]


vakiot = (venttiilit, huoneet, kartoitus)
aikaa = 26  
sijainti = "AA"
paine = 0
paras_kombo = 0
komboja_yht = 0

ihten_avainniput = itertools.combinations(venttiilit.keys(), 7)
for ihten_avaimet in ihten_avainniput:
    norsun_avaimet = venttiilit.keys() - ihten_avaimet
    # print(f"Ihten avaimet: {ihten_avaimet}\nNorsun avaimet: {norsun_avaimet}")
    ihten_venttiilit = {huoneet[huone].nimi: huoneet[huone] for huone in ihten_avaimet}
    norsun_venttiilit = {huoneet[huone].nimi: huoneet[huone] for huone in norsun_avaimet}
    ihten_paras = huoneeseen((ihten_venttiilit, huoneet, kartoitus), [], sijainti, aikaa, paine)
    norsun_paras = huoneeseen((norsun_venttiilit, huoneet, kartoitus), [], sijainti, aikaa, paine)
    yhteensa_paras = ihten_paras + norsun_paras
    paras_kombo = max(paras_kombo, yhteensa_paras)
    komboja_yht += 1
    pass

aika_lopussa = time.time()
print(paras_kombo)
print(f"Aikaa meni {aika_lopussa - aika_alussa}")
print(f"Komboja oli yhteensä {komboja_yht}")