jono = []
with open("data.txt") as f:
    i = 0
    for r in f:
        jono.append((i, int(r.strip()) * 811589153))
        i += 1


for kak in range(10):
    print(f"Kierros {kak} / 9 menossa")
    for i in range(len(jono)):
        for j in range(len(jono)):
            if jono[j][0] == i:
                indeksi = j
                break
        liikkuva = jono.pop(indeksi)
        liike = liikkuva[1]
        uusi_paikka = indeksi + liike

        if uusi_paikka < 0:
            uusi_paikka = abs(uusi_paikka)
            uusi_paikka = uusi_paikka % len(jono)
            uusi_paikka = - uusi_paikka
            uusi_paikka += len(jono)

        if uusi_paikka > len(jono):
            uusi_paikka = uusi_paikka % len(jono)

        if uusi_paikka == len(jono) or uusi_paikka == 0:
            jono.append(liikkuva)
        else:
            jono.insert(uusi_paikka, liikkuva)
        # print([j[1] for j in jono])



for i in range(len(jono)):
    if jono[i][1] == 0:
        nollan_paikka = i
        break
luvut = []
for i in range(1, 4):
    luvut.append(jono[(nollan_paikka + 1000 * i) % len(jono)][1])

print(luvut)
print(f"Vastaus on {sum(luvut)}")
