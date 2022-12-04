with open("data.txt") as f:
    parit = []
    for r in f:
        (eka, toka) = r.strip().split(",")[0:2]
        pari = [[int(n) for n in eka.split("-")], [int(n) for n in toka.split("-")]]
        parit.append(pari)

leikkaavia = 0

for pari in parit:
    if pari[0][0] >= pari[1][0] and pari[0][0] <= pari [1][1]:
        leikkaavia += 1
    elif pari[0][1] >= pari[1][0] and pari[0][1] <= pari [1][1]:
        leikkaavia += 1
    elif pari[1][0] >= pari[0][0] and pari[1][0] <= pari [0][1]:
        leikkaavia += 1
    elif pari[1][1] >= pari[0][0] and pari[1][1] <= pari [0][1]:
        leikkaavia += 1

print(f"Tonttujen alueet leikkaavat {leikkaavia} parilla")