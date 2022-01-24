# Escreva uma função que verifica se duas listas são iguais.

def lista_igual(list_1, list_2):
    if list_1 == list_2:
        return True
    else:
        return False

lista_a = [3, 2, 1, 4, 5, '6']
lista_b = [3, 2, 1, 4, 5, '6']

if lista_igual(lista_a, lista_b):
    print('É igual')
else:
    print('É diferente')