import random

longueur_railroad = 50
railroad = ["_"] * longueur_railroad
railroad[0] = "T"
railroad[-1] = "Terminus"
max_energie = 100
energie = max_energie
energie_use = 10
max_charge = 3
nb_recharges = 5
recharge = 10     #boucle random.randint(range(railroad)) outpout = railroad[index]  boucle
caisse = 9
lot_caisse = 5
perte_energie = 5
emplacement_recharges = 0
emplacement_caisse = 0
reste_energie = 100


def Emplacement_re():
    for i in range(5):
        emplacement_recharges = random.randint(1, 49)
        if emplacement_recharges == emplacement_recharges:
            emplacement_recharges = random.randint(1, 49)
        while railroad[emplacement_recharges] == railroad[-1]:
            emplacement_recharges = random.randint(1, 49)
        railroad[emplacement_recharges] = "R"


def Caisses():
    for i in range(5):
        emplacement_caisse = random.randint(1, 49)
        railroad[emplacement_caisse] = str(random.randint(1, 9))
        if emplacement_caisse == emplacement_caisse:
            emplacement_caisse = random.randint(1, 49)
        while railroad[emplacement_caisse] == "R" or railroad[emplacement_caisse] == railroad[-1]:
            emplacement_caisse = random.randint(1, 49)
       
#def rammassage_caisses():
    

def Deplacement(mouv):
    reste_energie = 
    for i in railroad:
        railroad[mouv + mouv] = "T"
        railroad[mouv - mouv] = "_"
        reste_energie = reste_energie - (energie_use * mouv)
    return(railroad, mouv, reste_energie)

Emplacement_re()
Caisses()

while railroad[-1] != "T" or energie > 0:
    mouv = int(input("De combien de rails voulez-vous déplacer le train??"))
    Deplacement(mouv)
    print(' '.join(railroad))
    print(reste_energie)
    if railroad[-1] == "T":
        print("bravo vous êtes bien arrivé(e) !")
    elif energie == 0:
        print("le train est tombée en panne !")
















#def Deplacement(max_energie, energie, perte_energie):
    #for i in 
