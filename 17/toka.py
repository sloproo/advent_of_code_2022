import time
alku = time.time()

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

sykli_loytynyt = False
for i in range(1000000000000):
    if sykli_loytynyt:
        break
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
            print(f"Tähän mennessä siis kiviä on pudonnut {len(erot)} sykliä eli " 
            + f"{len(erot)} sykliä * {len(suunnat) * 5} kiveä / sykli.\n" 
            + f"Samat kuin 1. - 4. sykli (indeksointi lähtee nollasta) ovat uudestaan järjestysnumeroiltaan\n" 
            + f"{len(erot) - 5} - {len(erot) - 1} . Syklin pituus on siis {len(erot) - 5} - 1 = {len(erot) - 3 - 1} * {len(suunnat) * 5} kiveä")

            print(f"Kiviä on tässä vaiheessa pudotettu {i+1} kappaletta.")
            sykli = erot[1:-4]
            sykli_loytynyt = True
        pass
    if sykli_loytynyt:
        break

    # print(f"Palikka {i} pudotettu\n")
    pass

sykli2 = [77730, 77732, 77726, 77709, 77744, 77741, 77721, 77733, 77730, 77745, 77745, 77725, 77747, 77728, 77725, 77717, 77738, 77734, 77734, 77723, 77727, 77751, 77734, 77736, 77739, 77738, 77725, 77724, 77718, 77743, 77741, 77713, 77738, 77735, 77740, 77744, 77737, 77733, 77732, 77727, 77709, 77740, 77740, 77730, 77724, 77726, 77747, 77742, 77734, 77751, 77725, 77720, 77717, 77732, 77737, 77743, 77717, 77733, 77737, 77740, 77742, 77737, 77732, 77730, 77727, 77714, 77737, 77743, 77723, 77733, 77730, 77742, 77748, 77725, 77746, 77731, 77722, 77715, 77742, 77729, 77735, 77726, 77726, 77748, 77736, 77738, 77738, 77736, 77725, 77725, 77717, 77746, 77739, 77712, 77739, 77734, 77743, 77742, 77738, 77733, 77730, 77727, 77715, 77735, 77743, 77725, 77728, 77723, 77745, 77749, 77732, 77750, 77723, 77720, 77718, 77738, 77732, 77744, 77717, 77730, 77743, 77737, 77740, 77736, 77734, 77728, 77729, 77717, 77737, 77739, 77722, 77734, 77732, 77740, 77748, 77728, 77744, 77730, 77724, 77715, 77739, 77732, 77733, 77726, 77729, 77748, 77733, 77740, 77741, 77733, 77724, 77724, 77719, 77743, 77741, 77712, 77739, 77732, 77743, 77744, 77736, 77734, 77729, 77726, 77714, 77738, 77743, 77725, 77729, 77725, 77744, 77749, 77729, 77750, 77723, 77721, 77720, 77738, 77732, 77738, 77723, 77727, 77743, 77740, 77740, 77734, 77733, 77727, 77731, 77720, 77735, 77739, 77721, 77735, 77733, 77740, 77744, 77731, 77744, 77729, 77724, 77714, 77738, 77736, 77731, 77723, 77735, 77745, 77732, 77742, 77744, 77727, 77728, 77720, 77724, 77739, 77743, 77716, 77738, 77730, 77743, 77740, 77737, 77734, 77731, 77726, 77713, 77736, 77745, 77723, 77730, 77725, 77743, 77751, 77727, 77752, 77722, 77724, 77720, 77735, 77736, 77735, 77721, 77728, 77745, 77742, 77735, 77735, 77736, 77725, 77731, 77717, 77741, 77737, 77720, 77736, 77731, 77745, 77742, 77733, 77739, 77731, 77722, 77716, 77736, 77738, 77731, 77723, 77731, 77746, 77737, 77739, 77750, 77718, 77731, 77717, 77727, 77738, 77744, 77716, 77737, 77735, 77740, 77739, 77740, 77731, 77733, 77723, 77712, 77742, 77743, 77721, 77731, 77726, 77746, 77748, 77723, 77754, 77724, 77724, 77720, 77734, 77736, 77736, 77721, 77724, 77751, 77741, 77735, 77732, 77737, 77728, 77727, 77716, 77744, 77737, 77717, 77738, 77733, 77743, 77741, 77734, 77737, 77730, 77726, 77714, 77737, 77741, 77731, 77723, 77727, 77747, 77741, 77731, 77755, 77719, 77729, 77715, 77728, 77740, 77742, 77717, 77737, 77735, 77739, 77741, 77739]
if sykli == sykli2:
    print("Jes, syklin mätsäys osui")
else:
    print("Saattans")
    print(f"Syklin pituuden pitäisi olla {len(sykli2)}, mutta se on {len(sykli)}")
    raise ValueError("Väärin leikattu sykli kun haetaan mätsääviä pudoteltavista")

koko = 1000000000000
blokki = len(suunnat) * 5
sykleihin = koko - blokki
syklin_pituus = len(sykli) * blokki
print(f"Alkun jälkeen sykleihin ja niiden jälkeisiin jää kiviä: {sykleihin}")
print(f"Syklin pituus kivinä: {syklin_pituus}")
sykleja = sykleihin // syklin_pituus
syklin_kasvu = sum(sykli)
print(f"Syklin aikana korkeus kasvaa {syklin_kasvu}")
print(f"Täysiä syklejä: {sykleja}")
sykleista_yli = sykleihin % syklin_pituus
print(f"Syklien loputtua jäljelle jää vielä {sykleista_yli} kiveä")

sykleista = sykleja * syklin_kasvu
muuten = 3285320
vastaus = sykleista + muuten
print(f"Vastaus on sykleistä {sykleista} + muuten {muuten} = {vastaus}")
loppu = time.time()
print(f"Aikaa kului {loppu - alku} sekuntia")
# Ykkösen jämiä

# print("Palikat pudotettu\nTorni:")
# for i in range(len(torni)):
#     print(torni[-i])

# print(f"Tornin korkeus = {len(torni) - 1 + baseline}")
# print(f"(Jäljelläolevan tornin korkeus: {len(torni) -1} , baseline: {baseline}")