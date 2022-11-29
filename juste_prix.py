from random import randrange
#l'utilisateur peut choisir quel niveau de difficulté
niveau = int(input('entrez le niveaux de difficulté entre 1 a 3 '))
#je prepare les constantes que j'aurais besoin
vmin = 0
match niveau:
    case 1 :
        vmax = 100
    case 2 :
        vmax = 1000
    case 3 :
        vmax = 1500
    
compteur = 0
proposition = 0 
prix = randrange(vmin, vmax)

#je prepare la boucle tant que avec 3 condition si plus grand si plus petit ou si il a trouvée
while proposition != prix :
    print('choisir entre 1 et',vmax)
    proposition = int(input( ''))
    compteur += 1
    if proposition < prix :
        print('le prix est plus élevé que votre proposition')
        vmin = proposition
    elif proposition > prix :
        print('le prix est plus bas que votre proposition')
        vmax = proposition
    else:
        print('bravo vous avez réussie a trouvée le prix mystère',prix,'avec', compteur, 'propositions.')

            