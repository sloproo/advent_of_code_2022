import string, copy

def liiku(y: int, x: int, vanha_suunta: str, liike: tuple[int, str]) -> tuple[int, int, str]:
    if y == 99 and x == 90:
        pass
    matka = liike[0]
    kaannos = liike[1]
    suunnat = ["u", "r", "d", "l"]
    if kaannos == "R" and vanha_suunta == "l":
        uusi_suunta = "u"
    elif kaannos == "L" and vanha_suunta == "u":
        uusi_suunta = "l"
    elif kaannos == "L":
        uusi_suunta = suunnat[suunnat.index(vanha_suunta)-1]
    elif kaannos == "R":
        uusi_suunta = suunnat[suunnat.index(vanha_suunta)+1]
    elif kaannos == "E":
        uusi_suunta = vanha_suunta

    while matka > 0:
        if suunta == "r":
            if x+1 >= len(kartta[y]):
                for x_2 in range(len(kartta[y])):
                    if kartta[y][x_2] == " ":
                        continue
                    elif kartta[y][x_2] == "#":
                        return (y, x, uusi_suunta)
                    elif kartta[y][x_2] == ".":
                        x = x_2
                        matka -= 1
                        break
            elif kartta[y][x+1] == ".":
                x += 1
                matka -= 1
                nayttokartta[y][x] = ">"
            elif kartta[y][x+1] == "#":
                return (y, x, uusi_suunta)
            elif kartta[y][x+1] == " ":
                raise ValueError("Oikealla ei pitäisi tulla vastaan tyhjää")
        elif suunta == "l":
            if x-1 < 0 or kartta[y][x-1] == " ":
                for x_2 in range(len(kartta[y]) -1, -1, -1):
                    if kartta[y][x_2] == "#":
                        return (y, x, uusi_suunta)
                    elif kartta[y][x_2] == ".":
                        x = x_2
                        matka -= 1
                        break
            elif kartta[y][x-1] == ".":
                x -= 1
                matka -= 1
            elif kartta[y][x-1] == "#":
                return y, x, uusi_suunta
        elif suunta == "u":
            if y == 0 or kartta[y-1][x] == " ":
                for y_2 in range(len(kartta)-1, 0, -1):
                    if len(kartta[y_2]) -1 < x or kartta[y_2][x] == " ":
                        continue
                    elif kartta[y_2][x] == "#":
                        return (y, x, uusi_suunta)
                    elif kartta[y_2][x] == ".":
                        y = y_2
                        matka -= 1
                        break
            elif kartta[y-1][x] == "#":
                return (y, x, uusi_suunta)
            elif kartta[y-1][x] == ".":
                y -= 1
                matka -= 1
        elif suunta == "d":
            if y + 1 == len(kartta) or len(kartta[y+1]) -1 < x or kartta[y+1][x] == " ":
                for y_2 in range(0, len(kartta)):
                    if kartta[y_2][x] == "#":
                        return (y, x, uusi_suunta)
                    elif kartta[y_2][x] == " ":
                        continue
                    elif kartta[y_2][x] == ".":
                        y = y_2
                        matka -= 1
                        break
            elif kartta[y+1][x] == "#":
                return (y, x, uusi_suunta)
            elif kartta[y+1][x] == ".":
                y += 1
                matka -= 1
    return (y, x, uusi_suunta)

kartta = []

with open("data.txt") as f:
    for r in f:
        kartta.append([])
        for m in r.rstrip():
            if m == "":
                break
            kartta[-1].append(m)
    liikerotla = r

nayttokartta = copy.deepcopy(kartta)

numero_str = ""
liikkeet = []
for m in liikerotla:
    if m in string.digits:
        numero_str += m
    elif m in string.ascii_uppercase:
        liikkeet.append((int(numero_str), m))
        numero_str = ""
    elif m == "\n":
        liikkeet.append((int(numero_str), "E"))

for x_haku in range(len(kartta[0])):
    if kartta[0][x_haku] == ".":
        y, x = (0, x_haku)
        break
suunta = "r"
pass

for liike in liikkeet:
    print(f"Liikutaan ruudusta y= {y} , x= {x} suuntaan {suunta} {liike[0]} askelta, sitten käännös {liike[1]}")
    y, x, suunta = liiku(y, x, suunta, liike)
    pass



suuntapisteet = {"r": 0, "d": 1, "l": 2, "u": 3}


print(f"Ollaan sijainnissa y = {y} , x = {x} , naama osoittaa suuntaan {suunta}")
print(f"Koordinaatit lähtevät nollan sijaan ykkösestä, eli lisätään niihin 1: y = {y+1} ja x = {x+1}")
print(f"Naaman suunnasta {suunta} {suuntapisteet[suunta]} pistettä")
print(f"1000 * {y+1} + 4 * {x+1} + {suuntapisteet[suunta]} = {1000 * (y+1) + 4 *(x+1) + suuntapisteet[suunta]}")
