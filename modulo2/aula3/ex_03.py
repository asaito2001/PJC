"""
   Faça uma função que calcule o n-ésimo termo (aquele que fica na posição número n) da
   sequência de Fibonnaci.
"""
def fibonnaci(termo):
    a = 0
    b = 1
    for it in range(3, termo+1):
        c = a + b
        a = b
        b = c
    return c

termo = int(input('Digite o termo: '))
print(fibonnaci(termo))
        