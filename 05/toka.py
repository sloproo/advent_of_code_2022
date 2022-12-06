import string

# Tähän manuaalisesti montako pylvästä on. Laiskaa, tiedän.
pylvaat = [[] for _ in range(9)]

kaskyt = []

def ota(pylvaasta: int, maara: int) -> list:
    return pylvaat[pylvaasta - 1][:maara]

def poista(pylvaasta: int, maara: int) -> list:
    return pylvaat[pylvaasta - 1][maara:]

def lisaa(pylvaaseen: int, lisattava: list) -> list:
    return lisattava + pylvaat[pylvaaseen - 1]

with open("data.txt") as f:
    for r in f:
        if "[" in r:
            for i in range(1, len(r) + 1, 4):
                if r[i] in string.ascii_uppercase:
                    pylvaat[(i-1) // 4].append(r[i])
        else:
            f.readline()
            break

    for r in f:
            r_listana = r.strip().split(" ")
            kaskyt.append([int(r_listana[i]) for i in [1, 3, 5]])


for kasky in kaskyt:
    pylvaat[kasky[2] - 1] = lisaa(kasky[2], ota(kasky[1], kasky[0]))
    pylvaat[kasky[1] - 1] = poista(kasky[1], kasky[0])

for pylvas in pylvaat:
    print(pylvas[0], end="")
