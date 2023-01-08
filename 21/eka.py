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
        if apina[0] % apina[2] != 0:
            print("Eikä edes mennyt tasan")
            input("Paina enter: ")
        return apina[0] // apina[2]
    pass

with open("data.txt") as f:
    for r in f:
        nimi = r.split(":")[0]
        huuto = r.split(":")[1].strip()
        if huuto[0] in "0123456789":
            huuto = int(huuto)
        else:
            huuto = huuto.split(" ")
        apinat[nimi] = huuto
        pass

while type(apinat["root"]) != int:
    for eka in apinat.keys():
        if type(apinat[eka]) == int:
            continue
        elif type(apinat[eka][0]) == str or type(apinat[eka][2]) == str:
            haettavat = [haettava for haettava in [0, 2] if type(apinat[eka][haettava]) == str]
            for haettava in haettavat:
                if type(apinat[apinat[eka][haettava]]) == int:
                    apinat[eka][haettava] = apinat[apinat[eka][haettava]]
        else:
            if type(apinat[eka][0]) == int and type(apinat[eka][2]) == int:
                apinat[eka] = laske(apinat[eka])

print(f"Apinan nimeltä root luku on {apinat['root']}")
