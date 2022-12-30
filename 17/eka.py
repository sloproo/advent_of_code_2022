import itertools, random

torni = ["#" *7]
korkeus = 0

def luo_palikka(muoto: str, korkeus: int) -> list:
    palikat = {"vaaka": [(korkeus + 4, i+2) for i in range(4)],
                "plus": [(korkeus + 5, 2), (korkeus + 5, 3), 
                        (korkeus + 5, 4), (korkeus + 6, 3), (korkeus + 4, 3)],
                "kulma": [(korkeus + 4, 2), (korkeus + 4, 3), (korkeus + 4, 4),
                        (korkeus + 5, 4), (korkeus + 6, 4)],
                "pysty": [(korkeus + 4 + i, 2) for i in range(4)],
                "nelio": [(korkeus + 4, 2), (korkeus + 5, 2),
                        (korkeus + 4, 3), (korkeus + 5, 3)]}
    return palikat[muoto]

def anna_muoto() -> str:
    muodot = ["vaaka", "plus", "kulma", "pysty", "nelio"]
    i = 0
    while True:
        yield muodot[i]
        i += 1
        if i == 5: i = 0

muotoilija = anna_muoto()

for i in range(2022):
    palikka = luo_palikka(next(muotoilija), korkeus)
    
    """
    Tähän väliin sit siirto ja pudotus
    """
    korkeus = len(torni) -1
    