class Humain:

    def __init__(self, name, drink="eau"):
        self.name = name
        self.drink = drink
        print(self.name + self.drink)

    def parler(self):
        print(f"Bonjour, je suis {self.name}. Ah ! Un bon verre de {self.drink}!, GLOUPS !")
    
        
    def quelEstTonNom(self):
        print(self.name)
        
    def Boissonpref(self):
        print(self.drink)

class dame(Humain):

    def __init__(self, name, etat="", robe="", drink="eau" ):
        super().__init__(name, drink)
        self.robe = robe
        self.etat = etat

    def couleur_robe(self):
        return (self.robe)

    def quelleEtat(self):
        print(self.etat)

    def change(self, newColor):
        self.robe = newColor
        print(f"Regardez ma nouvelle robe {self.couleur_robe()} !")
    
    def kidnapper(self):
        print("AAAAALEEEEED JPREFERE TOI TOIIIIII")

    def liberer(self, cowboy):
        print(f"Merci a toi {cowboy.name}")

    

class Brigand(Humain):

    def __init__(self, name, prison=bool, nbrenlevement=5, drink="eau", appa="mechant"):
        super().__init__(name, drink)
        self.appa = appa
        self.nbrenlevement = nbrenlevement
        self.prison = prison
      

    def Look(self):
        print(self.appa)

    def status(self):
        print(self.prison)
    
    def Enlevement(self, dame):
        print(f"Ah ah ! {dame.name}, tu es mienne désormais !" )
    
    def statistique(self):
        print(f"Nombre d'enlevement de {self.name} : {self.nbrenlevement}")

    def Capture(self, Cowboy):
        print(f"Damned, je suis fait ! {Cowboy.name}, tu m’as eu !")


class Cowboy(Humain) :

    def __init__(self, name, popularity=0, drink="eau", adjectif="the almighty"):
        super().__init__(name, drink)
        self.popularity = popularity
        self.adjectif = adjectif

    def shoot(self, brigand):
        print(f"Le {self.adjectif} {self.name} tire sur {brigand.name} PAN ! » et le cowboy s’exclame « Prend ça, rascal !")

    def rescue(self, dame):
        print(f"Ne vous inquietez pas {dame.name}, {self.adjectif} {self.name}, est la pour vous sauver !")



        


h = Humain("jean")
b = Brigand("WAZAA")
c = dame("sal")
d = Cowboy("yhwach")
b.Enlevement(c)
"""h.parler()"""
#h.quelEstTonNom()
#h.Boissonpref()
#b.Look()
#c.couleur_robe()
#b.status()
b.statistique()
c.change("rouge")
c.quelleEtat()
c.kidnapper()
d.shoot(b)
d.rescue(c)

