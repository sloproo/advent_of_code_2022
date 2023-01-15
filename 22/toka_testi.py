import string, copy

def alue(y: int, x: int) -> str:
    return string.ascii_lowercase[(y // sivun_pituus) *4 + x // sivun_pituus]
    
def kaanny(vanha_suunta: str, kaannos: str) -> str:
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
    return uusi_suunta

def liiku(y: int, x: int, vanha_suunta: str, oma_sivu: str, liike: tuple[int: str]) -> tuple[int, int, str]:
    matka = liike[0]
    kaannos = liike[1]

    print(f"Liikutaan sivulla {oma_sivu} suuntaan {vanha_suunta} , matkaa {matka} askelta, sitten käännytään suuntaan {kaannos}.")
    print(f"Liikkeelle lähdetään koordinaateista y = {y} , x = {x} ")

    while matka > 0:
        if vanha_suunta == "r":
            if x +1 >= sivun_pituus:
                return reunan_yli(y, x, matka -1, oma_sivu, vanha_suunta, kaannos)
            else:
                y, x, matka = seuraava_ruutu(y, x, oma_sivu, vanha_suunta, matka -1)
        elif vanha_suunta == "d":
            if y +1 >= sivun_pituus:
                return reunan_yli(y, x, matka -1, oma_sivu, vanha_suunta, kaannos)
            else:
                y, x, matka = seuraava_ruutu(y, x, oma_sivu, vanha_suunta, matka -1)
        elif vanha_suunta == "l":
            if x -1 < 0:
                return reunan_yli(y, x, matka -1, oma_sivu, vanha_suunta, kaannos)
            else:
                y, x, matka = seuraava_ruutu(y, x, oma_sivu, vanha_suunta, matka -1)
        elif vanha_suunta == "u":
            if y -1 < 0:
                return reunan_yli(y, x, matka -1, oma_sivu, vanha_suunta, kaannos)
            else:
                y, x, matka = seuraava_ruutu(y, x, oma_sivu, vanha_suunta, matka -1)
    y_abs, x_abs = absoluuttinen_koordinaatti(y, x, oma_sivu)
    uusi_suunta = kaanny(vanha_suunta, kaannos)
    print(f"Päästiin perille ruutuun y = {y} , x = {x} sivulla {oma_sivu} , seuraava suunta = {uusi_suunta}")
    return y_abs, x_abs, uusi_suunta

def reunan_yli(y: int, x: int, matka: int, vanha_sivu: str, suunta: str, kaannos: str) -> tuple[int, int, str]:
    print(f"Mennään reunan yli sivulta {vanha_sivu} suuntaan {suunta}")
    print(f"Askeleita jäljellä vielä {matka}")
    ylitykset = {}
    ylitykset["b"] = {"u": ("m", 3), "r": ("c", 0), "d": ("f", 0), "l": ("i", 2)}
    ylitykset["c"] = {"u": ("m", 0), "r": ("j", 2), "d": ("f", 3), "l": ("b", 0)}
    ylitykset["f"] = {"u": ("b", 0), "r": ("c", 1), "d": ("j", 0), "l": ("i", 1)}
    ylitykset["i"] = {"u": ("f", 3), "r": ("j", 0), "d": ("m", 0), "l": ("b", 2)}
    ylitykset["j"] = {"u": ("f", 0), "r": ("c", 2), "d": ("m", 3), "l": ("i", 0)}
    ylitykset["m"] = {"u": ("i", 0), "r": ("j", 1), "d": ("c", 0), "l": ("b", 1)}
    tuleva_sivu, kaannoksia = ylitykset[vanha_sivu][suunta]
    kaannetty_seuraava = kaanna_sivu(sivut[tuleva_sivu], kaannoksia)
    
    if (suunta == "r" and kaannetty_seuraava[y][0] == "#" 
        or suunta == "d" and kaannetty_seuraava[0][x] == "#"
        or suunta == "l" and kaannetty_seuraava[y][sivun_pituus-1] == "#"
        or suunta == "u" and kaannetty_seuraava[sivun_pituus-1][x] == "#"):
        y_abs, x_abs = absoluuttinen_koordinaatti(y, x, vanha_sivu)
        print("Reunan takana oli #, jäädään vanhalle sivulle")
        return y_abs, x_abs, kaanny(vanha_suunta, kaannos)
    
    elif (suunta == "r" and kaannetty_seuraava[y][0] == "." 
        or suunta == "d" and kaannetty_seuraava[0][x] == "."
        or suunta == "l" and kaannetty_seuraava[y][sivun_pituus-1] == "."
        or suunta == "u" and kaannetty_seuraava[sivun_pituus-1][x] == "."):
        if suunta == "r":
            y_uusi = y
            x_uusi = 0
        elif suunta == "d":
            y_uusi = 0
            x_uusi = x
        elif suunta == "l":
            y_uusi = y
            x_uusi = sivun_pituus-1
        elif suunta == "u":
            y_uusi = sivun_pituus-1
            x_uusi = x
        y_oikaistu, x_oikaistu = oikaise_koordinaatti(y_uusi, x_uusi, kaannoksia)
        uusi_suunta = reuna_suunnanmuutos(suunta, kaannoksia)
        return liiku(y_oikaistu, x_oikaistu, uusi_suunta, tuleva_sivu, (matka, kaannos))


    else:
        raise ValueError("Reunan yli outoon paikkaan")

def seuraava_ruutu(y: int, x: int, oma_sivu: str, suunta: str, matka: int) -> tuple[str, str, int]:
    if suunta == "u":
        uusi_y, uusi_x = y-1, x
    elif suunta == "r":
        uusi_y, uusi_x = y, x+1
    elif suunta == "d":
        uusi_y, uusi_x = y+1, x
    elif suunta == "l":
        uusi_y, uusi_x = y, x-1
    if sivut[oma_sivu][uusi_y][uusi_x] == "#":
        print(f"Tuli este vastaan ruudussa y = {uusi_y} , x = {uusi_x} sivulla {oma_sivu}")
        return (y, x, 0)
    elif sivut[oma_sivu][y][x] == ".":
        return uusi_y, uusi_x, matka

def reuna_suunnanmuutos(vanha_suunta: str, kaannoksia: int) -> str:
    suunnat = "uldruldru"
    return suunnat[suunnat.index(vanha_suunta):][kaannoksia]

def liiku_old(y: int, x: int, vanha_suunta: str, liike: tuple[int, str]) -> tuple[int, int, str]:
    matka = liike[0]
    kaannos = liike[1]
    uusi_suunta = kaanny(vanha_suunta, kaannos)

    while matka > 0:
        if vanha_suunta == "r":
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
            elif kartta[y][x+1] == "#":
                return (y, x, uusi_suunta)
            elif kartta[y][x+1] == " ":
                raise ValueError("Oikealla ei pitäisi tulla vastaan tyhjää")
        elif vanha_suunta == "l":
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
        elif vanha_suunta == "u":
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
        elif vanha_suunta == "d":
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

def anna_kirjain_hieno() -> str:
    kirjaimet = string.ascii_lowercase
    i = 0
    while True:
        yield kirjaimet[i]
        i += 4
        if i // 4 > 3:
            i = (i + 1)  % 4

def anna_kirjain() -> str:
    kirjaimet = string.ascii_lowercase
    i = 0
    while True:
        yield kirjaimet[i]
        i += 1

def kartta_sivuiksi(kartta: list) -> dict:
    sivut = {}
    for y in range(0, sivun_pituus * 4, sivun_pituus):
        for x in range(0, sivun_pituus * 4, sivun_pituus):
            if x >= len(kartta[y]):
                sivu = [[" " for _ in range(sivun_pituus)] for __ in range(sivun_pituus)]
            else:
                sivu = [kartta[y + lisaa][x:x+sivun_pituus+1] for lisaa in range(sivun_pituus)]
            # except IndexError:
            #     sivu = [["fff" for _ in range(50)] for __ in range(50)]
            sivut[next(antaja)] = sivu
    return sivut

def nayta_sivu(sivu: list):
    for rivi in sivu:
        for merkki in rivi:
            print(merkki, end="")
        print()

def kaanna_sivu(sivu: list, kertoja: int) -> list:
    for _ in range(kertoja):
        kaannetty = []
        for x in range(len(sivu[0])):
            uusi_rivi = []
            for y in range(len(sivu) -1, -1, -1):
                uusi_rivi.append(sivu[y][x])
            kaannetty.append(uusi_rivi)
        sivu = copy.deepcopy(kaannetty)
    return sivu

def oikaise_koordinaatti(y: int, x: int, oikaisuja: int) -> tuple[int, int]:
    # kertoja = {"u": 0, "r": 1, "d": 2, "l": 3}
    for _ in range(oikaisuja):
        x_uusi = y
        y_uusi = sivun_pituus-1 - x
        y = y_uusi
        x = x_uusi
    return (y, x)

def absoluuttinen_koordinaatti(y: int, x: int, sivu: str) -> tuple[int, int]:
    if y > sivun_pituus-1 or x > sivun_pituus-1:
        raise ValueError("Koordinaatit pielessä")
    x += (string.ascii_lowercase.index(sivu) % 4) * sivun_pituus
    y += (string.ascii_lowercase.index(sivu) // 4) * sivun_pituus
    return (y, x)

def koordinaatin_sivu(y: int, x: int) -> str:
    palautettava = string.ascii_lowercase[(y // sivun_pituus) * 4:][x // sivun_pituus]
    if palautettava not in ["b", "c", "f", "i", "j", "m"]:
        raise ValueError("Koordinaatti arpakuution og sivujen ulkopuolelta")
    return palautettava

def abs_koordinaatti_sivumuodossa(y: int, x: int) -> tuple[int, int, str]:
    sivu = koordinaatin_sivu(y, x)
    y = y % sivun_pituus
    x = x % sivun_pituus
    return (y, x, sivu)


kartta = []
antaja = anna_kirjain()

with open("alku.txt") as f:
    for r in f:
        if r == "\n":
            break
        else:
            kartta.append([m for m in r.rstrip()])
    liikerotla = f.readline()
sivun_pituus = 4
sivut = kartta_sivuiksi(kartta)


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
vanha_suunta = "r"

for liike in liikkeet:
    y_s, x_s, vanha_sivu = abs_koordinaatti_sivumuodossa(y, x)
    y, x, vanha_suunta = liiku(y_s, x_s, vanha_suunta, vanha_sivu, liike)
    pass



suuntapisteet = {"r": 0, "d": 1, "l": 2, "u": 3}


print(f"Ollaan sijainnissa y = {y} , x = {x} , naama osoittaa suuntaan {vanha_suunta}")
print(f"Koordinaatit lähtevät nollan sijaan ykkösestä, eli lisätään niihin 1: y = {y+1} ja x = {x+1}")
print(f"Naaman suunnasta {vanha_suunta} {suuntapisteet[vanha_suunta]} pistettä")
print(f"1000 * {y+1} + 4 * {x+1} + {suuntapisteet[vanha_suunta]} = {1000 * (y+1) + 4 *(x+1) + suuntapisteet[vanha_suunta]}")
