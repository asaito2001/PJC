"""
    Máscara para primos: Dada uma lista de números inteiros, determine uma nova lista,
    com a mesma quantidade de elementos, de modo que as posições em que havia um número
    primo, sejam preenchidas com o número 1 e as demais posições, com o número 0.
"""
def eh_primo(numero):
    primo = 1
    if numero > 1:
        for it in range(2, numero+1):
            if numero % it == 0:
                primo += 1
        if primo == 2:
            return True
    return False


def mascara_primos(lista):
    lista_primos = list()
    for num in numeros:
        if eh_primo(num):
            lista_primos.append(1)
        else:
            lista_primos.append(0)
    return lista_primos


numeros = [1, 4, 7, 9, 0, 23, 73, 25]
print(mascara_primos(numeros))



