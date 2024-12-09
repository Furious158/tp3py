class Humain:

    def __init__(self, name, drink="eau"):
        self.name = name
        self.drink = drink
        print(self.name + self.drink)

    def parler(self):
        print(f"Bonjour, je suis {self.name}. Ah ! Un bon verre d'{self.drink}!, GLOUPS !")

    def presentation(self):
        print(f"Bonjour, je suis {self.name} et j'aime l'{self.drink}")
    
        
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

    def quelEstTonNom(self):
        print(f"Miss {self.name}")
    
    def presentation(self):
        super().presentation()
        print(f"Regardez ma belle robe de couleur {self.couleur_robe()} ")

    

class Brigand(Humain):

    def __init__(self, name, prison=bool, nbrenlevement=5,bounty=100, drink="eau", appa="mechant"):
        super().__init__(name, drink)
        self.appa = appa
        self.nbrenlevement = nbrenlevement
        self.prison = prison
        self.bounty = bounty
      

    def Look(self):
        print(self.appa)

    def status(self):
        print(self.prison)
    
    def Enlevement(self, dame):
        print(f"Ah ah ! {dame.name}, tu prefere moi ou ta mere !" )
    
    def statistique(self):
        print(f"Nombre d'enlevement de {self.name} : {self.nbrenlevement}")

    def quelEstTonNom(self):
        print(f"{self.name} le {self.appa}")

    def presentation(self):
       super().presentation()
       print(f"j'ai l'air {self.appa}, et j'ai deja kidnappé {self.nbrenlevement} dames !")
       print(f"Ma tête est mise a pris {self.bounty}$")



class Cowboy(Humain) :

    def __init__(self, name, popularity=2, drink="whisky", adjectif="the almighty"):
        super().__init__(name, drink)
        self.popularity = popularity
        self.adjectif = adjectif
       

    def shoot(self, brigand):
        print(f"Le {self.adjectif} {self.name} tire sur {brigand.name} PAN ! et le cowboy s’exclame « Prend ça, rascal !")

    def rescue(self, dame):
        print(f"Ne vous inquietez pas {dame.name}, {self.adjectif} {self.name}, est la pour vous sauver !")

    def Capture(self):
        print(f"Damned, je suis fait ! {self.name}, tu m’as eu !")

    def quelEstTonNom(self):
       print(f"{self.name}")

    def presentation(self):
        super().presentation()
        print(f"Je suis {self.name} aussi connu sous le nom de {self.adjectif} {self.name}, ma popularité est de {self.popularity}")
    
class Barman(Humain) :
    def __init__(self, name,barname="", drink="vin"):
        super().__init__(name, drink)
        self.barname = barname

    def serv(self):
        print(f"Tenez ! voici un verre de votre boisson favorite {self.drink}")

    def presentation(self):
        super().presentation()
        print(f"je suis {self.name}")


        


h = Humain("jean")
b = Brigand("WAZAA")
c = dame("femme")
d = Cowboy("yhwach")
b.Enlevement(c)
c.kidnapper()
d.rescue(c)
d.Capture()
b.quelEstTonNom()
c.quelEstTonNom()
d.quelEstTonNom()
c.change("rouge")
c.presentation()
b.presentation()
d.presentation()

"""h.parler()"""
#h.quelEstTonNom()
#h.Boissonpref()
#b.Look()

#b.status()
#b.statistique()
#c.quelleEtat()
#c.kidnapper()
#d.shoot(b)
#d.rescue(c)

