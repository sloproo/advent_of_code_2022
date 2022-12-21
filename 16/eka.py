import apu

class Huone:
    def __init__(self, nimi: str, paine: int, reitit: list):
        self.nimi = nimi
        self.paine = paine
        self.reitit = reitit
    def __repr__(self) -> str:
        return f"nimi: {self.nimi} , paine: {self.paine} , reitit: {self.reitit} .\n"

huoneet = {}
with open("data.txt") as f:
    for r in f:
        sanat = r.strip().split(" ")
        nimi = sanat[1]
        paine = int(sanat[4][5:-1])
        reitit = [sana.replace(",", "") for sana in sanat[9:]]
        huoneet[nimi] = Huone(nimi, paine, reitit)

huoneiden_nimet = [huone for huone in huoneet.keys()]

kartoitus = apu.kartoita(huoneet)
print("jou")
pass            