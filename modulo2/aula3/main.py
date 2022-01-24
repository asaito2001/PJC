from matematica import area_triangulo, PI
# import matematica as mat


a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

area = area_triangulo(a, b, c)
print("Valor aproximado de pi é: {}".format(PI))
print('Área do triângulo é: {}'.format(area))