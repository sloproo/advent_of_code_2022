import copy, ast

def vertaa_listoja(eka: list, toka: list) -> int:
    vastaus = 0
    print(f"Verrataan paria\n{eka}\n\n{toka}\n")
    for i in range(max((len(eka), len(toka)))):
        if i == len(eka):
            print("Ekasta loppuu pituus")
            vastaus = 1
        elif i == len(toka):
            print("Tokasta loppuu pituus")
            vastaus = 2
        
        elif eka[i] == toka[i]:
            continue
        
        elif type(eka[i]) == type(toka[i]):
            if type(eka[i]) == int:
                print(f"Verrataan lukuja {eka[i]} ja {toka[i]}")
                if eka[i] == toka[i]:
                    print("Verrattavat luvut/listat olivat samat, pass " + 
                        "(äskeinen continue tässä oli ehkä virhe)")
                    pass
                elif eka[i] < toka[i]:
                    vastaus = 1
                    print(f"Vastaus oli {vastaus}")
                elif eka[i] > toka[i]:
                    vastaus = 2
                    print(f"Vastaus oli {vastaus}")
                else:
                    raise ValueError("Numerot eivät vertautuneet")
            elif type(eka[i]) == list:
                vastaus = vertaa_listoja(copy.deepcopy(eka[i]), copy.deepcopy(toka[i]))
        
        else: #eka[i] ja toka[i] eri tyyppiä
            if type(eka[i]) == int:
                eka[i] = [eka[i]]
            elif type(toka[i]) == int:
                toka[i] = [toka[i]]
            else:
                raise ValueError("Eri tyypit sekaisin")
            vastaus = vertaa_listoja(copy.deepcopy(eka), copy.deepcopy(toka))
        
        if vastaus != 0:
            print(f"Vastaus oli {vastaus}")
            return vastaus
        
        if vastaus == 0:
            print(f"No nyt meni pieleen")
            input("Höhöööö")

with open("data.txt") as f:
    parit = []
    pari = []
    for r in f:
        pari.append(ast.literal_eval(r.strip()))
        if len(pari) == 2:
            parit.append(pari)
            pari = []
            f.readline()

vastaukset = []
vastaustuplet = []
for i in range(len(parit)):
    vastaus = vertaa_listoja(copy.deepcopy(parit[i][0]), copy.deepcopy(parit[i][1]))
    print(f"Paria\n{parit[i][0]} ja\n{parit[i][1]}\n verratessa vastaus oli {vastaus}")
    # _ = input("Paina enter: ")
    print("\n" * 80)
    vastaukset.append(vastaus)
    vastaustuplet.append((i, vastaus))

oikein_menneiden_indeksit= []
oikeiden_indeksien_summa = 0
for i in range(len(vastaukset)):
    if vastaukset[i] == 1:
        oikein_menneiden_indeksit.append(i)
        oikeiden_indeksien_summa += i+1

kasvatetut_indeksit = [ind + 1 for ind in oikein_menneiden_indeksit]


print(f"Oikeassa järjestyksessä olleiden parien indeksien summa on {oikeiden_indeksien_summa}")
print(f"Toisin sanoen {sum(kasvatetut_indeksit)}")
print(f"Oikein menivät parit: {oikein_menneiden_indeksit}")

