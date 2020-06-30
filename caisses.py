import random


longueur_railroad = 50
railroad = ["_"] * longueur_railroad
railroad[0] = "T"
railroad[-1] = "Terminus"
position_train = railroad[0]
max_energie = 50
energie = max_energie
energie_use = 1
max_charge = 3
nb_recharges = 5
recharge = 10
listes_recharges = []      #boucle random.randint(range(railroad)) outpout = railroad[index]  boucle
recharge = 0
caisse = 9
lot_caisse = 5
perte_energie = 5
emplacement_recharges = 0
emplacement_caisse = 0



def Emplacement_re():
    for i in range(5):
        emplacement_recharges = random.randint(1, 49)
        while emplacement_recharges != emplacement_recharges:
            if emplacement_recharges == emplacement_recharges:
                emplacement_recharges = random.randint(1, 49)
            elif railroad[emplacement_recharges] == railroad[-1] or ("1", '2', '3', '4', '5'):
                emplacement_recharges = random.randint(1, 49)
        railroad[emplacement_recharges] = "R"



def Caisses():
    for i in range(5):
        emplacement_caisse = random.randint(1, 49)
        railroad[emplacement_caisse] = str(random.randint(1, 5))
        while emplacement_caisse != emplacement_caisse:
            if emplacement_caisse == emplacement_caisse:
                emplacement_caisse = random.randint(1, 49)
            elif railroad[emplacement_caisse] == "R" or railroad[emplacement_caisse] == railroad[-1]:
                emplacement_caisse = random.randint(1, 49)
            
        #if emplacement_recharges in railroad:

def Deplacement(mouv):
    for i in railroad:
        railroad[mouv] = "T"
        railroad[mouv - 1] = "_"
        energie -= energie_use * mouv
        return railroad






Emplacement_re()
Caisses()


print(' '.join(railroad))

