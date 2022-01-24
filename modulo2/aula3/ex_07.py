"""
    Implemente a criptografia de strings usando a cifra de César. 
    Há uma sequência de vídeos no canal que explicam sobre esse assunto.
    Não tem problema seguir os vídeos. 
"""
msg = 'Alexandre'
chave = 3

def criptografia(msg, chave):
    n = 128
    cifrada = ''
    for letra in msg:
        indice = ord(letra)
        nova_letra = chr((indice + chave) % n)
        cifrada = cifrada + nova_letra
    return cifrada

print(criptografia(msg, chave))
print(msg)

'''
    decifrada = ''
    for letra in cifrada:
        indice = ord(letra)
        nova_letra = chr((indice - chave) % n)
        decifrada = decifrada + nova_letra

    print(decifrada)
'''