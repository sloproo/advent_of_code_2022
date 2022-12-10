def r(sijainti: list) -> list:
    return [sijainti[0]+1, sijainti[1]]

def l(sijainti: list) -> list:
    return [sijainti[0]-1, sijainti[1]]

def u(sijainti: list) -> list:
    return [sijainti[0], sijainti[1]+1]

def d(sijainti: list) -> list:
    return [sijainti[0], sijainti[1]-1]

def vertaa(origo: list, verrattava: list) -> list:
    return ([origo[0] - verrattava[0], origo[1] - verrattava[1]])

with open("data.txt") as f:
    paan_liikkeet = []
    for rivi in f:
        liike = rivi.strip().split(" ")
        paan_liikkeet.append((liike[0].lower(), int(liike[1])))

koysi = [[0, 0] for _ in range(10)]
hannan_sijainnit = {(0, 0)}

for (suunta, maara) in paan_liikkeet:
    for _ in range(maara):
        koysi[0] = locals()[suunta](koysi[0])
        for i in range(9):
            paa = koysi[i]
            hanta = koysi[i+1]
            hannasta_paahan = vertaa(paa, hanta)
            if ((abs(hannasta_paahan[0]) == 2 and abs(hannasta_paahan[1]) >= 1) or 
                (abs(hannasta_paahan[0]) >= 1 and abs(hannasta_paahan[1]) == 2)):
                    hanta = [hanta[0] + hannasta_paahan[0] // abs(hannasta_paahan[0]), 
                            hanta[1] + hannasta_paahan[1] // abs(hannasta_paahan[1])]
                    koysi[i+1] = hanta
                    if i == 8:
                        hannan_sijainnit.add((hanta[0], hanta[1]))
            elif (abs(hannasta_paahan[0]) == 2 and abs(hannasta_paahan[1]) == 0):
                hanta = [hanta[0] + hannasta_paahan[0] // abs(hannasta_paahan[0]), 
                        hanta[1]]
                koysi[i+1] = hanta
                if i == 8:
                    hannan_sijainnit.add((hanta[0], hanta[1]))
            elif (abs(hannasta_paahan[0]) == 0 and abs(hannasta_paahan[1]) == 2):
                hanta = ([hanta[0], hanta[1] + hannasta_paahan[1]
                        // abs(hannasta_paahan[1])])
                koysi[i+1] = hanta
                if i == 8:
                    hannan_sijainnit.add((hanta[0], hanta[1]))
            else:
                break

print(f"Häntä oli köyden heiluttelun myötä {len(hannan_sijainnit)} paikassa.")
