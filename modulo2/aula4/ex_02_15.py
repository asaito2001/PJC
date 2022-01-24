"""
    Trabalhar com arquivos de texto
"""
import os
# endereço relativo do arquivo - está na mesma pasta, diferindo apenas do nome do arquivo.
#arq_rel = open('modulo2/aula4/mensagem.txt')

# endereço absoluto
#arq_abs = open('/home/asaito2001/repos/python3/PJC/Modulo2/aula4/mensagem.txt')

# endereço utilizando a biblioteca os do python
caminho = os.path.join('modulo2', 'aula4', 'mensagem.txt')
arq_os = open(caminho)

#conteudo = arq_rel.read()
#print(conteudo)

"""
-=-=-=-= Exibir linha a linha do txt
linha = arq_abs.readline()
while linha:
    print(linha)
    linha = arq_abs.readline()
"""
print(arq_os.readlines()) # cria uma lista com as linhas como um termo
arq_os.close()