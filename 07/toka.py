import string

with open("data.txt") as f:
    tiedostot, hakemistot, sijainti = [], [], []
    for r in f:
        if r[0] == "$":
            if r[2:4] == "cd":
                liike = r.strip().split(" ")[2]
                if liike == "..":
                    sijainti = sijainti[:-1]
                else:
                    if liike == "/":
                        sijainti.append("root")
                    else:
                        sijainti.append(liike)
                if "/".join(sijainti) not in hakemistot:
                    hakemistot.append("/".join(sijainti))
            elif r[2:4] == "ls":
                continue
        elif r[0] in string.digits:
            koko, nimi = r.strip().split(" ")
            tiedostot.append(("/".join(sijainti), nimi, int(koko)))
        elif r[0:3] == "dir":
            pass
        else:
            print("Nyt tuli vastaan syötteessä jotain omituista")


hakemistojen_koot = []
for hakemisto in hakemistot:
    hakemiston_koko = 0
    for tiedosto in tiedostot:
        if hakemisto == tiedosto[0][:len(hakemisto)]:
            hakemiston_koko += tiedosto[2]
    hakemistojen_koot.append((hakemisto, hakemiston_koko))

kapasiteetti = 70000000
kaytetty = sum(tiedosto[2] for tiedosto in tiedostot)
vapaana = kapasiteetti - kaytetty
tarvittava = 30000000
vapautettava = tarvittava - vapaana

hakemistot_koon_mukaan = sorted(hakemistojen_koot, key=lambda hakemisto: hakemisto[1])
poistettava = [sopiva for sopiva in hakemistot_koon_mukaan if sopiva[1] >= vapautettava][0]

print(f"Poistettava hakemisto on {poistettava[0]}, jonka koko on {poistettava[1]}")