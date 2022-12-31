def luo_palikka(palikan_nro: int, baseline: int) -> list:
    palikat = {"vaaka": [(baseline + 4, i+2) for i in range(4)],
                "plus": [(baseline + 5, 2), (baseline + 5, 3), 
                        (baseline + 5, 4), (baseline + 6, 3), (baseline + 4, 3)],
                "kulma": [(baseline + 4, 2), (baseline + 4, 3), (baseline + 4, 4),
                        (baseline + 5, 4), (baseline + 6, 4)],
                "pysty": [(baseline + 4 + i, 2) for i in range(4)],
                "nelio": [(baseline + 4, 2), (baseline + 5, 2),
                        (baseline + 4, 3), (baseline + 5, 3)]}
    muodot = [avain for avain in palikat.keys()]
    return palikat[muodot[palikan_nro % 5]]

def liikuta(palikka: list, torni: list, suunta: str, baseline: int) -> list:
    torni = kasvata(torni)
    for y, x in palikka:
        if suunta == "<":
            if x - 1 == -1:
                return palikka
            elif torni[y - baseline][x-1] == "#":
                return palikka
        elif suunta == ">":
            if x + 1 == 7:
                return palikka
            elif torni[y - baseline][x+1] == "#":
                return palikka
        else:
            raise KeyError("Mahdoton suunta liikuttaessa")
    if suunta == "<":
        return [(y, x -1) for y, x in palikka]
    elif suunta == ">":
        return [(y, x +1) for y, x in palikka]

def pudota (palikka: list, torni: list, baseline: int) -> tuple[list, list]:
    pysahtyi = False
    for y, x in palikka:
        if torni[y - baseline - 1][x] == "#" or y - 1 == baseline:
            pysahtyi = True
            break
        
    if pysahtyi:
        tyhja_rivi = [" " for _ in range(7)]
        for _ in range(4):
            torni.append(tyhja_rivi.copy())
        for (y, x) in palikka:
                torni[y - baseline][x] = "#"
        torni = siisti(torni)
        return (torni, [])
    else:
        laskenut_palikka = []
        for y, x in palikka:
            laskenut_palikka.append((y - 1, x))
        return (torni, laskenut_palikka)

def kasvata(torni: list) -> list:
    tyhja_rivi = [" " for _ in range(7)]
    for _ in range(8):
        torni.append(tyhja_rivi.copy())
    return torni

def tasoita(torni: list, baseline: int) -> tuple[list, int]:
    taysi_rivi = ["#" for _ in range(7)]
    for i in range(len(torni) - 1, 0, -1):
        if torni[i] == taysi_rivi:
            torni = torni[i:]
            baseline += i
            return (torni, baseline)
    return torni, baseline

def anna_suunta(suunnat: str) -> str:
    i = 0
    while True:
        yield suunnat[i]
        i += 1
        if i == len(suunnat): i = 0

def siisti(torni: list) -> list:
    tyhja_rivi = [" " for _ in range(7)]
    for _ in range(len(torni)):
        if torni[-1] == tyhja_rivi:
            torni.pop(-1)
        else:
            break
    return torni

def nayta(torni: list):
    for i in range(len(torni) -1, -1, -1):
        for m in torni[i]:
            print(m, end="")
        print()

with open("data.txt") as f:
    suunnat = f.readline().strip()
torni = [["#" for _ in range(7)]]
baseline = 0

taysi_rivi = ["#" for _ in range(7)]
suunnannayttaja = anna_suunta(suunnat)
korkeudet_syklin_jalkeen = [0]
erot = []

for i in range(1000000000000):
    palikka = luo_palikka(i, baseline + len(torni) - 1)
    while palikka != []:
        suunta = next(suunnannayttaja)
        palikka = liikuta(palikka, torni, suunta, baseline)
        # print(f"Siirretty suuntaan {suunta}")
        torni, palikka = pudota(palikka, torni, baseline)
        # print(f"Pudotettu{' asettui' if palikka == [] else ''}")
    # torni, baseline = tasoita(torni, baseline)
    torni = siisti(torni)
    # nayta(torni)

    if (i + 1) % (len(suunnat) * 5) == 0:
        # print(f"5 * {len(suunnat)} kiveä pudotettu")
        # print(f"Eroa edelliseen on {len(torni) -1 - korkeudet_syklin_jalkeen[-1]}")
        # print(f"Korkeus tässä vaiheessa on {len(torni) - 1} , lisätään listaan")
        erot.append(len(torni) -1 - korkeudet_syklin_jalkeen[-1])
        korkeudet_syklin_jalkeen.append(len(torni) - 1)
        
        if len(erot) > 6 and erot[-4:] == erot[1:5]:
            print(f"{i + 1} kiveä pudotettu")
            print(f"Edelliset neljä {len(suunnat) * 5} kiven joukkoa ovat " 
            + "kasvattaneet tornia saman verran kuin ensimmäistä seuraavat neljä"
            + "samankokoista joukkoa.\nSykli on siis nähtävillä. Tornin korkeuden"
            + "kasvut tällaisten joukkojen jälkeen:")
            print(erot)
            print(f"Kiviä on tässä vaiheessa pudotettu {i+1} kappaletta.")
        pass

    # print(f"Palikka {i} pudotettu\n")
    pass

print("Palikat pudotettu\nTorni:")
for i in range(len(torni)):
    print(torni[-i])

print(f"Tornin korkeus = {len(torni) - 1 + baseline}")
print(f"(Jäljelläolevan tornin korkeus: {len(torni) -1} , baseline: {baseline}")