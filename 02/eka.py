def omasta_pisteet(peli: tuple[str, str]) -> int:
    if peli[1] == "X":
        return 1
    elif peli[1] == "Y":
        return 2
    elif peli[1] == "Z":
        return 3
    else:
        print("Vääränlainen oma peliväline")

def voittopisteet(peli: tuple[str, str]) -> int:
    if peli[0] == "A":
        if peli[1] == "X":
            return 3
        elif peli[1] == "Y":
            return 6
        elif peli[1] == "Z":
            return 0
        else:
            print("vastustajalla kivi, oma väärin")
    elif peli[0] == "B":
        if peli[1] == "X":
            return 0
        elif peli[1] == "Y":
            return 3
        elif peli[1] == "Z":
            return 6
        else:
            print("vastustajalla paperi, oma väärin")
    elif peli[0] == "C":
        if peli[1] == "X":
            return 6
        elif peli[1] == "Y":
            return 0
        elif peli[1] == "Z":
            return 3
        else:
            print("vastustajalla sakset, oma väärin")
    else:
        print("Vastustajan ase rikki")

with open("data.txt") as f:
    pelit = []
    for r in f:
        pelit.append(tuple((r.strip()).split(" ")))

omat_pisteet = 0
for peli in pelit:
    omat_pisteet += omasta_pisteet(peli)
    omat_pisteet += voittopisteet(peli)

print(f"Omat pisteet: {omat_pisteet}")
