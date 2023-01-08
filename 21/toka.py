import copy
apinat = {}

def laske(apina: list) -> int:
    if apina[1] == "+":
        return apina[0] + apina[2]
    if apina[1] == "-":
        return apina[0] - apina[2]
    if apina[1] == "*":
        return apina[0] * apina[2]
    if apina[1] == "/":
        # print(f"Jakolasku, jaetaan {apina[0]} / {apina[2]}")
        # if apina[0] % apina[2] != 0:
        #     print("Eikä edes mennyt tasan")
        #     input("Paina enter: ")
        return apina[0] // apina[2]

def reverse(yhtalo: str, tavoite: int) -> int:
    osat = yhtalo.split(" ")
    if osat[0] == "aiempi":
        toisen_indeksi = 2
        toinen_luku = int(osat[2])
    elif osat[2] == "aiempi":
        toisen_indeksi = 0
        toinen_luku = int(osat[0])
    else:
        input("täällä ei pitäisi olla")
    operaattori = osat[1]
    # print(f"Käännetään yhtälö {osat} , tavoite on {tavoite}")
    if operaattori == "/":
        if toisen_indeksi == 0:
            return toinen_luku / tavoite
        elif toisen_indeksi ==2:
            return tavoite * toinen_luku
        print(f"Kerrotaan luvulla {toinen_luku}")
        return tavoite * toinen_luku
    if operaattori == "+":
        return tavoite - toinen_luku
    if operaattori == "-":
        if toisen_indeksi == 0:
            return toinen_luku - tavoite
        if toisen_indeksi ==2:
            return toinen_luku + tavoite
        
    if operaattori == "*":
        # print("kertolasku toisin päin")
        # print(f"edellinen jaettava = {edellinen} , toinen luku = {toinen_luku}")
        # print(f"Näiden jakojäännös on {tavoite % toinen_luku} eli jos != 0, ei mene tasan ja ollaan ongelmissa.")
        return tavoite / toinen_luku

with open("data.txt") as f:
    for r in f:
        nimi = r.split(":")[0]
        huuto = r.split(":")[1].strip()
        if huuto[0] in "0123456789":
            huuto = int(huuto)
        else:
            huuto = huuto.split(" ")
        apinat[nimi] = huuto
    orig_apinat = copy.deepcopy(apinat)

seurattavat = {"humn"}
mutkat = {"humn": "humn"}
operaatiot = []
while type(apinat["root"]) != int:
    for eka in apinat.keys():
        if type(apinat[eka]) == int:
            continue
        elif type(apinat[eka][0]) == str or type(apinat[eka][2]) == str:
            haettavat = [haettava for haettava in [0, 2] if type(apinat[eka][haettava]) == str]
            for haettava in haettavat:
                if apinat[eka][haettava] in seurattavat:
                    seurattavat.add(eka)
                if type(apinat[apinat[eka][haettava]]) == int:
                    apinat[eka][haettava] = apinat[apinat[eka][haettava]]
        else:
            if type(apinat[eka][0]) == int and type(apinat[eka][2]) == int:
                if eka in seurattavat:
                    # print(f"Tehdään seurannan alla oleva laskutoimitus, apinan {eka} arvo")
                    # print(f"Alun perin {eka} oli {orig_apinat[eka]}")
                    # print(f"Laskutoimitus on {apinat[eka]}")
                    # print(f"Joksi tulee {laske(apinat[eka])}")
                    seurannasta = []
                    for numero in [0, 2]:
                        if orig_apinat[eka][numero] in seurattavat:
                            seurannasta.append((orig_apinat[eka][numero], numero))
                    if len(seurannasta) != 1:
                        print("Erikoista, seurattavia ei ole 1 vaan 0 tai 2")
                    seurannasta = seurannasta[0]
                    pitempi = mutkat[seurannasta[0]]
                    if seurannasta[1] == 0:
                        liitettava = [pitempi, apinat[eka][1], str(apinat[eka][2])]
                        mutkat[eka] = "(" + " ".join(liitettava) + ")"
                        operaatiot.append("aiempi " + liitettava[1] + f" {liitettava[2]}")
                    elif seurannasta[1] == 2:
                        liitettava = [str(apinat[eka][0]), apinat[eka][1], pitempi]
                        mutkat[eka] = "(" + " ".join(liitettava) + ")"
                        operaatiot.append(f"{liitettava[0]} " + liitettava[1] + f" aiempi")
                    else:
                        input("Tänne ei pitäisi joutua, OK: ")
                    # print(mutkat)
                    
                apinat[eka] = laske(apinat[eka])

print(f"Apinan root alkuperäinen lasku oli {orig_apinat['root']}")

for i in [0, 2]:
    if orig_apinat['root'][i] in seurattavat:
        print(f"{orig_apinat['root'][i]} oli seurattavissa")
        # print(f"Sen arvo on {mutkat[orig_apinat['root'][i]]}")
        verrokin_juuret = mutkat[orig_apinat['root'][i]]
    if orig_apinat['root'][i] not in seurattavat:
        # print(f"Toisen luvun {orig_apinat['root'][i]} arvo taas oli {apinat[orig_apinat['root'][i]]}")
        tavoite = apinat[orig_apinat['root'][i]]

print(f"Eli\n\n{verrokin_juuret[1:-1]}\n\npitäisi olla yhtä kuin\n\n{tavoite} ")

edellinen = tavoite
for i in range(len(operaatiot)-2, -1, -1):
    # print(f"Seuraavaksi {operaatiot[i]} = {edellinen}")
    edellinen = reverse(operaatiot[i], edellinen)
    # print(f"Aiempi = {edellinen}")

print(f"Alussa huudettava numero on {int(edellinen)}")
