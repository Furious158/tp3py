class Humain:

    def __init__(self, name, drink="eau"):
        self.name = name
        self.drink = drink

    def parler(self, texte):
        print(f"{self.name} - {texte}")

    def presentation(self):
        print(f"Bonjour, je suis {self.name} et j'aime l'{self.drink}")
       
    def quelEstTonNom(self):
        print(self.name)
        

class dame(Humain):

    def __init__(self, name, robe="rouge", drink="lait" ):
        super().__init__(name, drink)
        self.robe = robe
        self.etat = "libre"

    def couleur_robe(self):
        return (self.robe)

    def quelleEtat(self):
        print(self.etat)

    def change(self, newColor):
        self.robe = newColor
        print(f"Regardez ma nouvelle robe {self.couleur_robe()} !")
    
    def kidnapper(self):
        self.etat = "captive"
        print("AAAAALEEEEED JPREFERE TOI TOIIIIII")

    def liberer(self, cowboy):
        self.etat = "libre"
        print(f"Merci a toi {cowboy.name}")

    def quelEstTonNom(self):
        print(f"Miss {self.name}")
    
    def presentation(self):
        print(f"Regardez ma belle robe de couleur {self.couleur_robe()} ")

    

class Brigand(Humain):

    def __init__(self, name, nbrenlevement=5,bounty=100, drink="Tord-Boyeaux", look="mechant"):
        super().__init__(name, drink)
        self.look = look
        self.nbrenlevement = nbrenlevement
        self.prison = False
        self.bounty = bounty
      

    def isinjail(self):
        print({self.prison})
        

    def Capture(self, Cowboy):
        self.prison = True
        self.parler(f"Damned, je suis fait {Cowboy.name}, tu m'as eu !")
    
    def Enlevement(self, dame):
        print(f"Ah ah ! {dame.name}, tu prefere moi ou ta mere !" )
    
    def statistique(self):
        print(f"Nombre d'enlevement de {self.name} : {self.nbrenlevement}")

    def quelEstTonNom(self):
        print(f"{self.name} le {self.appa}")

    def presentation(self):
       print(f"j'ai l'air {self.appa}, et j'ai deja kidnappé {self.nbrenlevement} dames !")
       print(f"Ma tête est mise a pris {self.bounty}$")



class Cowboy(Humain) :

    def __init__(self, name, popularity=0,drink="whisky", adjectif="the almighty"):
        super().__init__(name, drink)
        self.adjectif = adjectif
        self.popularity = popularity
        
    def shoot(self, brigand):
        print(f" {self.adjectif} {self.name} tire sur {brigand.name} PAN !")
        self.parler("Prend ca rascal !")
        
    def rescue(self, dame):
        self.popularity += 1
        print(f"Ne vous inquietez pas {dame.name}, {self.adjectif} {self.name}, est la pour vous sauver !")
        print(self.popularity)

    def Capture(self):
        print(f"Damned, je suis fait ! {self.name}, tu m’as eu !")

    def presentation(self):
        self.parler(f"Je suis {self.name} aussi connu sous le nom de {self.adjectif} {self.name}, ma popularité est de {self.popularity}")


    
class Barman(Humain) :
    def __init__(self, name, drink="vin"):
        super().__init__(name, drink)
        self.barname = name

    def serv(self, client):
        self.client = client
        print(f"Tenez ! voici un verre de votre boisson favorite {client.drink} Coco")

    def presentation(self):
        print(f"je suis {self.name} et je tiens le bar Chez {self.barname} Coco")




class sherif(Cowboy):
    def __init__(self, name, popularity=2, arrest=1, drink="whisky", adjectif="honest"):
        super().__init__(name, popularity, drink, adjectif)
        self.arrest = arrest

    def detain(self, brigand):
        self.arrest+=1
        print(f"Au nom de la loi, {brigand.name} je vous arrête !")
        print(self.arrest)

    def research(self, brigand):
        print(f"OYEZ OYEZ BRAVE GENS !! 200 $ à qui arrêtera {brigand.name} le brigand mort ou vif !")
    
    def presentation(self):
        print(f"je suis le Shérif {self.name}, j'ai deja arreté {self.arrest} brigand !")


        


h = Humain("jean")
b = Brigand("WAZAA")
c = dame("femme")
d = Cowboy("yhwach")
e = Barman("yokosho")
f = sherif("boulisse")
d.presentation()
c.presentation()
c.change("yellow")
c.presentation
d.presentation()
#b.Capture(f)
#d.shoot(b)
#c.presentation()
#f.detain(b)
#e.presentation()
#f.presentation()
#d.rescue(c)

#f.parler()
#b.Enlevement(c)
#c.kidnapper()
#d.rescue(c)
#d.Capture()
#b.quelEstTonNom()
#c.quelEstTonNom()
#d.quelEstTonNom()
#c.change("rouge")
#c.presentation()
#b.presentation()
#d.presentation()
#b.isinjail()
#e.serv(dame)

#h.parler()
#h.quelEstTonNom()
#h.Boissonpref()
#b.Look()

#b.status()
#b.statistique()
#c.quelleEtat()
#c.kidnapper()
#d.shoot(b)
#d.rescue(c)

