import string

def prioriteetti(esine: str) -> int:
        return string.ascii_letters.find(esine) + 1

with open("data.txt") as f:
    reput = []
    for reppu in f:
        reput.append(reppu.strip())

prioriteettien_summa = 0

for reppu in reput:
    osiot = (reppu[:len(reppu) // 2], reppu[len(reppu) // 2:])
    for esine in osiot[0]:
        if esine in osiot[1]:
            prioriteettien_summa += prioriteetti(esine)
            break

print(prioriteettien_summa)