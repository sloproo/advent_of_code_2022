def naapurit(x: int, y: int, z: int) -> list:
    palautettavat = []
    palautettavat.append((x+1, y, z))
    palautettavat.append((x-1, y, z))
    palautettavat.append((x, y+1, z))
    palautettavat.append((x, y-1, z))
    palautettavat.append((x, y, z+1))
    palautettavat.append((x, y, z-1))
    return palautettavat

vokselit = []
vapaita_sivuja = 0

with open("data.txt") as f:
    for r in f:
        x, y, z = (int(luku) for luku in r.strip().split(","))
        print(f"(x, y, z): ({x}, {y}, {z})")
        viereiset = naapurit(x, y, z)
        sivuja_tulossa = 6
        for naapuri in viereiset:
            if naapuri in vokselit:
                sivuja_tulossa -= 1
        vapaita_sivuja = vapaita_sivuja - 6 + (2 * sivuja_tulossa)
        vokselit.append((x, y, z))

print(f"Vapaita sivuja on {vapaita_sivuja}")


