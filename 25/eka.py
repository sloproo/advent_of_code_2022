def snafusta_dec(snafu: str) -> int:
    merkit = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    luku = 0
    for i in range(len(snafu)):
        luku += merkit[snafu[-(i+1)]] * (5 ** i)
    return luku

def dec_snafuksi(dec: int) -> str:
    luvut = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    palautettava = ""
    for i in range(1, 1000):
        if dec >= 5 ** i - pienempien_maksimi(i):
            continue
        else:
            suurin_eksponentti = i
            break
    for eks in range(suurin_eksponentti, -1, -1):
        for kerroin in range(-2, 3, 1):
            if (5 ** eks * kerroin) + pienempien_maksimi(eks) >= dec :
                palautettava += luvut[kerroin]
                dec -= kerroin * 5**eks
                break
        # print(f"Palautettava tässä vaiheessa: {palautettava}, desimaaleja tämän jälkeen vielä {eks-1} .")
        # print(f"Luvun saldo tässä kohtaa on: {dec}")
    if palautettava[0] == "0":
        palautettava = palautettava[1:]
    return palautettava

def pienempien_maksimi(eksponentti: int) -> int:
    return sum([2 * 5**j for j in range(eksponentti-1, -1, -1)])

snafujen_summa = 0
desimaaleina = []
with open("data.txt") as f:
    for r in f:
        desimaaleina.append(snafusta_dec(r.strip()))

print(f"Summa SNAFU-muodossa on {dec_snafuksi(sum(desimaaleina))}")
