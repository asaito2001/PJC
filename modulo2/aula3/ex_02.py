"""
    Escreva uma função que recebe um número inteiro (n) como argumento e responde
    a soma de todos os números inteiros de 1 até este n.
"""
from random import randint

def soma_inteiro(n):
    acumulado = 0
    for it in range(1, n+1):
        acumulado += it
    return acumulado

numero = randint(0, 100)
print(f'O acumulado de {numero} é {soma_inteiro(numero)}.')