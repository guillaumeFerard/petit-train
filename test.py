railroad = ["_"] * 20
railroad[0] = "T"
#railroad[0] = T
#railroad = ''.join(railroad)



def Deplacement(mouv):
    for i in railroad:
        railroad[mouv] = "T"
        railroad[mouv - 1] = "_"
        energie -= energie_use * mouv
        return railroad
        # print(' '.join(railroad))


        
