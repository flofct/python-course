from array import array

tableau = []
nombre = int(input("Quelle table souhaitez-vous afficher ? "))

for i in range(1,11):
    elements = int(i*nombre)
    if elements % 3 == 0:
        tableau.append(f'{elements} *')
    else:
        tableau.append(elements)
    
print(tableau)