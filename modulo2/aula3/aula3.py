#  REAPROVEITANDO CÓDIGOS COM FUNÇÕES

# A função responde com 1 dos 3 casos possíveis
# mas não amarra a resposta do programa com um print
def situacao_de_voto(idade):
    if idade >= 18 and idade < 70:
        return 'obrigatorio'
    elif idade >= 16:
        return 'facultativo'
    else:
        return 'proibido'
        
idade = int(input("Digite idade:"))
situacao = situacao_de_voto(idade)
# alternativa à formatação com f-string
# infelizmente, f-string é um recurso 
# não compatível com este ambiente 
print('Com {} anos, seu voto é {}'.format(idade, situacao))


def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def maximo(lista):
    maior = -999999999
    for n in lista:
        if n > maior:
            maior = n
    return maior


def media(lista):
    m = 0
    for n in lista:
        m += n
    return m / len(lista)


def fatorial(numero):
    produto = 1
    while numero > 0:
        produto *= numero
        numero -= 1
    return produto


# funcao str.find()
def buscar(lista, elemento):
    indice = None  # Valor especial do python que siginica "o nada"
    for it in range(0, len(lista)):
        if lista[it] == elemento:
            indice = it
    return indice
