import random


def easy_game():
    random_number = random.randint(1,10)
    tries = 1
    guess = int(input("Veuillez rentrer un chiffre entre 1 et 10 inclus : "))
    
    while guess != random_number:
        if guess > random_number:
            print(f'Le nombre est plus petit que {guess}')
        else:
            print(f'Le nombre est plus grand que {guess}')
        tries += 1
        guess = int(input("Veuillez rentrer un chiffre entre 1 et 10 inclus : "))
    
    if guess == random_number:
        print(f'Félicitations ! Vous avez trouvé en {tries} essais.')

def medium_game():
    random_number = random.randint(1,100)
    tries = 1
    guess = int(input("Veuillez rentrer un chiffre entre 1 et 100 inclus : "))
    
    while guess != random_number:
        if guess > random_number:
            print(f'Le nombre est plus petit que {guess}')
        if guess < random_number:
            print(f'Le nombre est plus grand que {guess}')
        tries += 1
        guess = int(input("Veuillez rentrer un chiffre entre 1 et 100 inclus : "))
    
    if guess == random_number:
        print(f'Félicitations ! Vous avez trouvé en {tries} essais.')

def hard_game():
    random_number = random.randint(1,1000)
    tries = 1
    guess = int(input("Veuillez rentrer un chiffre entre 1 et 1000 inclus : "))
    
    while guess != random_number:
        if guess > random_number:
            print(f'Le nombre est plus petit que {guess}')
        if guess < random_number:
            print(f'Le nombre est plus grand que {guess}')
        tries += 1
        guess = int(input("Veuillez rentrer un chiffre entre 1 et 1000 inclus : "))
    
    if guess == random_number:
        print(f'Félicitations ! Vous avez trouvé en {tries} essais.')