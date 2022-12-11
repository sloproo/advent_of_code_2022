import string
apinat = []

class Apina:
    def __init__(self, numero: int, esineet: list, operaattori: str, 
                operoitava: str, jakaja: int, kohde_t: int, kohde_f: int):
        self.numero = numero
        self.esineet = esineet
        self.operaattori = operaattori
        if operoitava[0] in string.digits:
            self.operoitava = int(operoitava)
        else:
            self.operoitava = operoitava
        self.jakaja = jakaja
        self.kohde_t = kohde_t
        self.kohde_f = kohde_f
        self.tarkastuksia = 0

    def tarkasta(self, esine:int) -> int:
        if self.operoitava == "old":
            kaytto_operoitava = esine
        elif type(self.operoitava) == int:
            kaytto_operoitava = self.operoitava
        else:
            raise TypeError(f"Menee esineen tarkastelu apinalta {self.numero} vituix")

        if self.operaattori == "+":
            self.tarkastuksia += 1
            return esine + kaytto_operoitava
        elif self.operaattori == "*":
            self.tarkastuksia += 1
            return esine * kaytto_operoitava
        else:
            raise TypeError(f"Menee esineen tarkastelu apinalta {self.numero} vituix")
        
    
    def kyllasty(self, esine: int) -> int:
        return esine // 3
    
    def vastaanota(self, esine: int):
        self.esineet.append(esine)
    
    def paata(self, esine: int):
        if esine % self.jakaja == 0:
            apinat[self.kohde_t].vastaanota(esine)
        else:
            apinat[self.kohde_f].vastaanota(esine)
    
    def kierros(self):
        for esine in self.esineet:
            esine = self.tarkasta(esine)
            esine = self.kyllasty(esine)
            self.paata(esine)
        self.esineet = []

with open("data.txt") as f:
    for r in f:
        if r == "\n":
            continue
        
        r = r.strip().split(" ")
        if r[0] == "Monkey":
            apinan_nro = int(r[1][:-1])
        elif r[0] == "Starting":
            alkuesineet = [int(esine.replace(",", "")) for esine in r[2:]]
        elif r[0] == "Operation:":
            operaattori = r[4]
            operoitava = r[5]
        elif r[0] == "Test:":
            jakaja = int(r[-1])
        elif r[0] == "If":
            if r[1] == "true:":
                kohde_t = int(r[-1])
            elif r[1] == "false:":
                kohde_f = int(r[-1])
                apinat.append(Apina(apinan_nro, alkuesineet, operaattori, operoitava,
                                    jakaja, kohde_t, kohde_f))
                alkuesineet = []
                operaattori, operoitava, jakaja, kohde_t, kohde_f = [None for _ in range(5)]
        else:
            print("Tänne ei pitäisi päätyä")


for _ in range(20):
    for apina in apinat:
        apina.kierros()

bisnesluokitukset = sorted([apina.tarkastuksia for apina in apinat], reverse=True)
for apina in apinat:
    print(f"Apinan {apina.numero} bisnesluokitus = {apina.tarkastuksia}")

print(f"Kahden suurimman bisneluokituksen {bisnesluokitukset[0]} ja " +
     f"{bisnesluokitukset[1]} tulo on {bisnesluokitukset[0] * bisnesluokitukset[1]}")
    
