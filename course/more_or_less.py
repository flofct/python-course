import random
from fonction import easy_game
from fonction import medium_game
from fonction import hard_game

    
difficulty = int(input("Choisisez le difficulté souhaitée : \n Tapez 1 pour la difficulté facile, tapez 2 pour la difficultée intermédiaire ou tapez 3 pour la diffulté maximale. "))

while difficulty != 1 and difficulty != 2 and difficulty != 3:
    print("Veuillez rentrer un nombre valide.")
    difficulty = int(input("Choisisez le difficulté souhaitée : \n Tapez 1 pour la difficulté facile, tapez 2 pour la difficultée intermédiaire ou tapez 3 pour la diffulté maximale. "))

if difficulty == 1:
    easy_game()
elif difficulty == 2:
    medium_game()
elif difficulty == 3:
    hard_game()







