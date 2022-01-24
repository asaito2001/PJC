import math

PI = math.pi
VALOR_MINIMO = -9999999999


def perimetro_triangulo(a, b, c):
    """ Calcula o perímetro de um triângulo """
    return a + b + c


def validar(a, b, c):
    if abs(b - c) < a and a < b + c:
        return True
    return False


def triangulo_eh_valido(a, b, c):
    if validar(a, b, c) and validar(b, c, a) and validar(c, a, b):
        return True
    return False


def area_triangulo(a, b, c):
    if triangulo_eh_valido(a, b, c):
        # semi-perimetro
        p = perimetro_triangulo(a, b, c)/2
        # área pela fórmula de Heron
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return area
    # triângulo impossível (inválido)
    return 0


def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


def maximo(lista):
    maior = VALOR_MINIMO
    for n in lista:
        if n > maior:
            maior = n
    return maior


def media(lista):
    m = 0
    for n in lista:
        # acumulando a soma da lista
        m = m + n
    # retorna a média
    return m/len(lista)


def fatorial(n):
    produto = 1
    while n > 0:
        produto = produto * n
        n = n - 1
    return produto


if __name__ == "__main__":    
    n = int(input('Digite um número: '))
    print('{}! é {}'.format(n, fatorial(n)))