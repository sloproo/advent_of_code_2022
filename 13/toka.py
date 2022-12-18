import copy, ast

def vertaa_listoja(eka: list, toka: list) -> int:
    vastaus = 0
    # print(f"Verrataan paria\n{eka}\n\n{toka}\n")
    for i in range(max((len(eka), len(toka)))):
        if i == len(eka):
            # print("Ekasta loppuu pituus")
            vastaus = 1
        elif i == len(toka):
            # print("Tokasta loppuu pituus")
            vastaus = 2
        
        elif eka[i] == toka[i]:
            continue
        
        elif type(eka[i]) == type(toka[i]):
            if type(eka[i]) == int:
                # print(f"Verrataan lukuja {eka[i]} ja {toka[i]}")
                if eka[i] == toka[i]:
                    print("Verrattavat luvut/listat olivat samat, pass " + 
                        "(äskeinen continue tässä oli ehkä virhe)")
                    pass
                elif eka[i] < toka[i]:
                    vastaus = 1
                    # print(f"Vastaus oli {vastaus}")
                elif eka[i] > toka[i]:
                    vastaus = 2
                    # print(f"Vastaus oli {vastaus}")
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
            # print(f"Vastaus oli {vastaus}")
            return vastaus
        
        if vastaus == 0:
            print(f"No nyt meni pieleen")
            input("Höhöööö")

with open("data.txt") as f:
    paketit = [[[2]], [[6]]]
    for r in f:
        if r == "\n":
            continue
        rivi = ast.literal_eval(r.strip())
        for i in range(len(paketit)):
            if vertaa_listoja(rivi, copy.deepcopy(paketit[i])) == 1:
                paketit.insert(i, ast.literal_eval(r.strip()))
                break
        else:
            paketit.append(ast.literal_eval(r.strip()))

eka = paketit.index([[2]])
toka = paketit.index([[6]])

print(f"Jakajapaketit ovat riveillä {eka+1} ja {toka+1} . {eka+1} * {toka+1} = {(eka+1) * (toka+1)} .")