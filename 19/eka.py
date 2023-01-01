class Kaava:
    def __init__(self, ore_orea: int, savi_orea: int, obs_orea: int, obs_savea:int,
                geo_orea: int, geo_obsia: int):
                    self.ore_orea = ore_orea
                    self.savi_orea = savi_orea
                    self.obs_orea = obs_orea
                    self.obs_savea = obs_savea
                    self.geo_orea = geo_orea
                    self.geo_obsia = geo_obsia
                    self.orea = 0
                    self.savea = 0
                    self.obsia = 0
                    self.geoja = 0
                    self.robotit = [0, 0, 0, 0]
                    self.aikaa = 26

    def rakenna_ore(self) -> bool:
        if self.orea >= self.ore_orea:
            self.robotit[0] += 1
            self.orea -= self.ore_orea
            return True
        else:
            return False

    def rakenna_savi(self) -> bool:
        if self.orea >= self.savi_orea:
            self.robotit[1] += 1
            self.orea -= self.savi_orea
            True
        else:
            return False
    
    def rakenna_obs(self) -> bool:
        if self.orea >= self.obs_orea and self.savea >= self.obs_savea:
            self.robotit[2] += 1
            self.orea -= self.obs_orea
            self.savea -= self.obs_savea
            return True
        else:
            return False

    def rakenna_geo(self) -> bool:
        if self.orea >= self.geo_orea and self.obsia >= self.geo_obsia:
            self.robotit[3] += 1
            self.orea -= self.geo_orea
            self.obs -= self.geo_obsia
            return True
        else:
            return False

    def keraa(self):
        self.orea += self.robotit[0]
        self.savea += self.robotit[1]
        self.obsia += self.robotit[2]
        self.geoja += self.robotit[3]



pass
