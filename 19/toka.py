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
                    self.maksimit = []
                    self.maksimitarpeet()

    def maksimitarpeet(self):
        self.maksimit = [0 for _ in range(4)]
        for robo in range(4):
            for materiaali in range(3):
                if self.hinnat[robo][materiaali] > self.maksimit[materiaali]:
                    self.maksimit[materiaali] = self.hinnat[robo][materiaali]
    
    def keraa(self, robot: list, rahat: list) -> list:
        rahat = [rahat[i] + robot[i] for i in range(4)]
        return rahat

    def valmista(self, valmistuva: int, robot: list) -> list:
        robot[valmistuva] += 1
        return robot

    def maksa(self, rahat: list, robo: list) -> list:
        for i in range(4):
            rahat[i] -= self.hinnat[robo][i]
        return rahat

    def rahat_riittaa(self, rahat: list, robo: int) -> bool:
        for i in range(4):
            if rahat[i] < self.hinnat[robo][i]:
                return False
        else:
            return True

    def turhaa(self, rakennettava: int, robot: list) -> bool:
        for i in range(4):
            if self.hinnat[rakennettava][i] != 0 and robot[i] == 0:
                return True
        else:
            return False

    def pyorita(self) -> int:
        maksimi = 0
        for seuraava in range(1, -1, -1):
                talta = self.kierros([0, 0, 0, 0], [1, 0, 0, 0], seuraava, 32)
                maksimi = max([maksimi, talta])
        return maksimi
    
    def kierros(self, rahat: list, robot: list, rakennettava: int, aikaa: int) -> int:
        rakennettu = False
        if self.rahat_riittaa(rahat, rakennettava):
            rakentuva = rakennettava
            rahat = self.maksa(rahat, rakennettava)
        else:
            rakentuva = None
        rahat = self.keraa(robot, rahat)
        if rakentuva != None:
            robot = self.valmista(rakentuva, robot)
            rakennettu = True
        pass
        if aikaa == 1:
            return rahat[3]
        else:
            if rakennettu:
                saadut_geot = [rahat[3]]
                if self.rahat_riittaa(rahat, 3):
                    talta = self.kierros(rahat.copy(), robot.copy(), 3, aikaa -1)
                    saadut_geot.append(talta)
                else:
                    for seuraava in range(2, -1, -1):
                        if self.rahat_riittaa(rahat, 3) and seuraava != 3:
                            continue
                        if robot[seuraava] == self.maksimit[seuraava] and seuraava != 3:
                            continue
                        if self.turhaa(seuraava, robot):
                            continue
                        talta = self.kierros(rahat.copy(), robot.copy(), seuraava, aikaa -1)
                        saadut_geot.append(talta)
                return max(saadut_geot)
            else:
                talta = self.kierros(rahat.copy(), robot.copy(), rakennettava, aikaa -1)
                return max(rahat[3], talta)


kaavat = {}
with open("data.txt") as f:
    for r in f:
        r = r.strip().split(" ")
        kaavan_nrot = [int(luku) for luku in [r[1][:-1], r[6], r[12], r[18], r[21],
        r[27], r[30]]]
        kaavat[kaavan_nrot[0]] = (Kaava(*kaavan_nrot))

saatavat = []
saatavat_kerrottuna = 1
for i in range(1, 4):
    saatava = kaavat[i].pyorita()
    saatavat.append(saatava)
    saatavat_kerrottuna *= saatava

pass
print(saatavat)
print(saatavat_kerrottuna)

print(f"Vastaus on {saatavat_kerrottuna} ")
