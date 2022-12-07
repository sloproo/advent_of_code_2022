import string

def prioriteetti(esine: str) -> int:
        return string.ascii_letters.find(esine) + 1

with open("data.txt") as f:
    reput = []
    for reppu in f:
        reput.append(reppu.strip())

prioriteettien_summa = 0

for i in range(0, len(reput), 3):
    for merkki in string.ascii_letters:
        if merkki in reput[i] and merkki in reput[i+1] and merkki in reput[i+2]:
            prioriteettien_summa += prioriteetti(merkki)
            break

print(prioriteettien_summa)
