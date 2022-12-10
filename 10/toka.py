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
    for sykli in range(1, 241):
        if (sykli -1) % 40 >= rek - 1 and (sykli -1) % 40 <= rek + 1:
            print("█", end="")
        else:
            print(" ", end="")
        if (sykli) % 40 == 0:
            print()
        # print(f"Sykli {sykli} , rekisteri {rek}")
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
