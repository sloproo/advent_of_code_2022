class Kaava:
    def __init__(self, nro: int, ore_orea: int, savi_orea: int, obs_orea: int,
                obs_savea:int, geo_orea: int, geo_obsia: int):
                    self.nro = nro
                    self.hinnat = [[0 for __ in range(4)] for _ in range(4)]
                    self.hinnat[0][0] = ore_orea
                    self.hinnat[1][0] = savi_orea
                    self.hinnat[2][0] = obs_orea
                    self.hinnat[2][1] = obs_savea
                    self.hinnat[3][0] = geo_orea
                    self.hinnat[3][2] = geo_obsia
                    self.rahat = [0 for _ in range(4)]
                    self.robotit = [1, 0, 0, 0]
                    self.rakennettava = None
                    self.rakentuva = None
                    self.paamaara = 1
                    self.aikaa = 26
                    self.maksimit = []
                    self.maksimitarpeet()

    def maksimitarpeet(self):
        self.maksimit = [0 for _ in range(4)]
        for robo in range(4):
            for materiaali in range(3):
                if self.hinnat[robo][materiaali] > self.maksimit[materiaali]:
                    self.maksimit[materiaali] = self.hinnat[robo][materiaali]

    def rakentumaan(self, robo: int) -> bool:
        for i in range(4):
            if self.rahat[i] >= self.hinnat[robo][i]:
                continue
            else:
                return False
        self.rakentuva = robo
        return True
    
    def keraa(self):
        for i in range(4):
            self.rahat[i] += self.robotit[i]

    def valmista(self):
        if self.rakentuva == None:
            pass
        else:
            self.robotit[self.rakentuva] += 1
            self.rakentuva = None

    def paamaara(self):
        for i in range(1, 4):
            if self.robotit[i] == 0:
                self.paamaara = i
                return
            else:
                self.paamaara = 3
    
    def kriittisin(self) -> int:
        kriittisyydet = [0 for _ in range(3)]
        if self.paamaara == 1:
            return 0
        for i in range(4):
            if self.hinnat[self.paamaara][i] == 0:
                pass
            else:
                kriittisyydet[i] = self.hinnat[self.paamaara][i] - self.robotit[i]
        suurin = max(kriittisyydet)
        if kriittisyydet.count(suurin) > 1:
            kriittiset = [i for i in range(4) if kriittisyydet[i] == suurin]
            return max(kriittiset)
        else:
            return kriittisyydet.index(suurin)

    def ehtiiko(self, alempi: int) -> bool:
        puuttuvat = [self.hinnat[self.paamaara][i] - self.rahat[i] for i in range(4)]
        odotusajat = []
        for i in range(4):
            if puuttuvat[i] // self.robotit[i] % 1 != 0:
                odotusajat.append(puuttuvat[i] // self.robotit[i] + 1)
            else:
                odotusajat.append(puuttuvat[i] // self.robotit[i])
        pisin_odotus = max(odotusajat)
        if odotusajat.count(pisin_odotus) ==  1:
            pisimpaan_odotettava = odotusajat.index(pisin_odotus)
        else:
            odotettavat = [i for i in range(4) if odotusajat[i] == pisin_odotus]
            tarvittavin = max([])

        
        




    
    # def odotus(self, robo: int) -> int:
    #     puuttuvat = [self.hinnat[robo][i] - self.rahat[i] for i in range(4)]
    #     odotusta = [0 for _ in range(4)]
    #     for i in range(4):
    #         if puuttuvat[i] > 0:
    #             odotusta[i] = puuttuvat[i] // self.robotit[i]
    #             if puuttuvat[i] / self.robotit[i] % 1 != 0:
    #                 odotusta[i] += 1
            
    
    # def ehtiiko(self, robo: int) -> bool:

    
    # def paata_rakennettava(self):
    #     if self.robotit[2] == 0:
    #         if self.robotit[1] == 0:


    def paata_rakennettava(self):
        if self.rakentumaan(3):
            return
        """
        todo: funktio, joka selvittää nopeimman tavan tehdä obs-robotti
              Ehkä rekursiivisesti funktio, joka selvittää nopeimman tavan
              tehdä savirobotti sitä ennen (ore-robotteja alle vai suoraan savi)
              Tai ehkä yleisluontoisempi funktio, joka antaa nopeimmin määrät
              x ja y resursseja z ja å?
        """
        # self.rakenna_ore()

    def kierros(self):
        self.paata_rakennettava()
        self.keraa()
        self.valmista()
        self.aikaa -= 1
    
    def pyorita(self) -> int:
        while self.aikaa > 0:
            self.kierros()
        return self.geoja
    





kaavat = {}
with open("alku.txt") as f:
    for r in f:
        r = r.strip().split(" ")
        kaavan_nrot = [int(luku) for luku in [r[1][:-1], r[6], r[12], r[18], r[21],
        r[27], r[30]]]
        kaavat[kaavan_nrot[0]] = (Kaava(*kaavan_nrot))

ekasta = kaavat[1].pyorita()
print(ekasta)
























    # def rakenna_ore(self) -> bool:
    #     if self.orea >= self.ore_orea:
    #         self.rakentuva = 0
    #         self.orea -= self.ore_orea
    #         return True
    #     else:
    #         return False

    # def rakenna_savi(self) -> bool:
    #     if self.orea >= self.savi_orea:
    #         self.rakentuva = 1
    #         self.orea -= self.savi_orea
    #         return True
    #     else:
    #         return False
    
    # def rakenna_obs(self) -> bool:
    #     if self.orea >= self.obs_orea and self.savea >= self.obs_savea:
    #         self.rakentuva = 2
    #         self.orea -= self.obs_orea
    #         self.savea -= self.obs_savea
    #         return True
    #     else:
    #         return False

    # def rakenna_geo(self) -> bool:
    #     if self.orea >= self.geo_orea and self.obsia >= self.geo_obsia:
    #         self.rakentuva = 3
    #         self.orea -= self.geo_orea
    #         self.obsia -= self.geo_obsia
    #         return True
    #     else:
    #         return False
