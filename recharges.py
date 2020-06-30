import random


longueur_railroad = 50
railroad = ["_"] * longueur_railroad
railroad[0] = "T"
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



def Emplacement_re():
    for i in range(nb_recharges):
        emplacement_recharges = random.randint(1,49)
        while emplacement_recharges != emplacement_recharges:
            if emplacement_recharges == emplacement_recharges:
                emplacement_recharges = random.randint(1, 49)
        railroad[emplacement_recharges] = "R"
        #if emplacement_recharges in railroad:

    print(print(' '.join(railroad)))



Emplacement_re()