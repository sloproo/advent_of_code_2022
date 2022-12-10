with open("data.txt") as f:
    kaskyt = []
    for r in f:
        if r.strip() == "noop":
            kaskyt.append("noop")
        elif r.strip().split(" ")[0][:4] == "addx":
            kaskyt.append(int(r.strip().split(" ")[1]))
        else:
            raise ValueError("Tiedoston luvussa outo rivi")

rek = 1
tois = False
i_kasky = 0
huomioitavien_summa = 0

try:
    for sykli in range(1, 5000):
        if sykli == 20 or (sykli - 20) % 40 == 0:
            print(f"Syklin {sykli} aikana rekisterin arvo on {rek}")
            print(f"Rekisteriin tallennetaan {sykli} * {rek} = {sykli * rek}")
            huomioitavien_summa += sykli * rek
        if tois:
            rek += lisattavana
            tois = False
            continue
        elif kaskyt[i_kasky] == "noop":
            i_kasky += 1
            continue
        else:
            lisattavana = kaskyt[i_kasky]
            i_kasky += 1
            tois = True
        
except IndexError:
    print(f"Lista tuli käsiteltyä loppuun viimeisen ajetun syklin ollessa n. {sykli-1}")

print(f"Kiinnostavissa kohdissa talteen otettujen signaalin vahvuuksien summa on {huomioitavien_summa}")
