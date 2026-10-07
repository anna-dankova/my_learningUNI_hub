'''Imamo parkirno garažo, ki ima določeno kapaciteto avtomobilov in
trenutno število parkiranih avtomobilov. Uporabi razrede in metode za
naslednje funkcionalnosti:
● zacetno_stanje … začetno število avtomobilov v garaži
● vstop … število avtomobilov, ki želijo vstopiti v garažo
● odhod … število avtomobilov, ki zapustijo garažo
● stanje … trenutno število avtomobilov v garaži'''


class Parking:
    def __init__(self, kapaciteta):
        self.kapaciteta=kapaciteta
        kapaciteta=0

    def zacetno_stanje(self,avtomobili):
        if avtomobili<=self.kapaciteta :
            self.avtomobili=avtomobili
        else:
            print('ni vec prostora')
        self.stanje()
    def vstop(self,zelijo_vstopiti):
        if self.avtomobili + zelijo_vstopiti > self.kapaciteta :
            print(' ni vec prostora ')
            self.avtomobili = self. kapaciteta
        else:
            self.avtomobili+= zelijo_vstopiti
        self.stanje()

    def odhod(self, odhajajo):
        if self.avtomobili < odhajajo :
            print('napaka pri vnosu')
        else:
            self.avtomobili -= odhajajo
        self.stanje()
    def stanje(self):
        print(f'Zdaj v garazi je {self.avtomobili} avtomobilov')
        prostor= self.kapaciteta-self.avtomobili
        print(f'v garazi je se {prostor} mest ')

p=Parking( 15)
p.zacetno_stanje(3)
p.vstop(6)
p.odhod(3)
p.odhod(10)
p.stanje()