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

kohtuulliset = sum([koko[1] for koko in hakemistojen_koot if koko[1] <= 100000])
print(kohtuulliset)