apinat = {}

def laske(apina: list) -> int:
    if apina[1] == "+":
        return apina[0] + apina[2]
    if apina[1] == "-":
        return apina[0] - apina[2]
    if apina[1] == "*":
        return apina[0] * apina[2]
    if apina[1] == "/":
        print(f"Jakolasku, jaetaan {apina[0]} / {apina[2]}")
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
            for toka in apinat.keys():
                if eka == toka:
                    continue
                if type(apinat[toka]) != int:
                    for huuto in [0, 2]:
                        if apinat[toka][huuto] == eka:
                            apinat[toka][huuto] = apinat[eka]
        else:
            if type(apinat[eka][0]) == int and type(apinat[eka][2]) == int:
                apinat[eka] = laske(apinat[eka])

print(f"Apinan nimeltä root luku on {apinat['root']}")