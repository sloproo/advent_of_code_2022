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
                    self.rakentuva = None
                    self.aikaa = 26

    def rakenna(self, robo: int) -> bool:
        for i in range(4):
            if self.rahat[i] >= self.hinnat[robo][i]:
                continue
            else:
                return False
        self.rakentuva = robo
        return True

    def aikaa_obsin_riittamiseen(self) -> int:
        if (self.hinnat[3][2] - self.rahat[2]) % self.robotit[2] != 0:
            aikaa_obsin_riittamiseen = (self.geo_obsia - self.obsia) // self.robotit[2] + 1
        else:
            aikaa_obsin_riittamiseen = (self.geo_obsia - self.obsia) // self.robotit[2]
        return aikaa_obsin_riittamiseen

    def keraa(self):
        for i in range(4):
            self.rahat[i] += self.robotit[i]

    def valmista(self):
        if self.rakentuva == None:
            pass
        else:
            self.robotit[self.rakentuva] += 1
            self.rakentuva = None

    def paata_rakennettava(self):
        if self.rakenna(3):
            return
        aikaa_obsiin = self.aikaa_obsin_riittamiseen()
        """
        todo: funktio, joka selvittää nopeimman tavan tehdä obs-robotti
              Ehkä rekursiivisesti funktio, joka selvittää nopeimman tavan
              tehdä savirobotti sitä ennen (ore-robotteja alle vai suoraan savi)
              Tai ehkä yleisluontoisempi funktio, joka antaa nopeimmin määrät
              x ja y resursseja z ja å?
        """
        

            
        if self.rakenna_obs():
            return
        if self.rakenna_savi():
            return
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
