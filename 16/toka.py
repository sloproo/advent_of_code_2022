import apu2, time
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
venttiilit = dict(sorted(venttiilit.items(), key= lambda venttiili: venttiili[1].paine, reverse=True))
# venttiilit = [huoneet[huone] for huone in huoneet.keys() if huoneet[huone].paine > 0]

vakiot = (venttiilit, huoneet, kartoitus)
aikaa = 26  
sijainti = "AA"
paine = 0

paine = apu2.kierros(("AA", 0), ("AA", 0), vakiot, ["AA"], 
        ["AA"], aikaa, 0)
aika_lopussa = time.time()
print(paine)
print(f"Aikaa meni {aika_lopussa - aika_alussa}")
