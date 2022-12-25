def snafusta_dec(snafu: str) -> int:
    merkit = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    luku = 0
    for i in range(len(snafu)):
        luku += merkit[snafu[-(i+1)]] * (5 ** i)
    return luku


def pienempien_maksimi(eksponentti: int) -> int:
    return sum([2 * 5**j for j in range(eksponentti-1, -1, -1)])

pass
while True:
    print(snafusta_dec(input("Anna snafu, se decinä on: ")))