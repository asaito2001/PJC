import os

def ler_arquivo(arquivo):
    caminho = os.path.join('modulo2', 'aula4', arquivo)
    f = open(caminho)
    conteudo = f.read()
    print(conteudo)
    f.close()

# abrir para escrita
novo_arquivo = open('modulo2/aula4/codigo.txt', 'wt')
novo_arquivo.write('O ser e o nada.\n')
novo_arquivo.close()

# abrir para adicionar
novo_arquivo = open('modulo2/aula4/codigo.txt', 'at')
novo_arquivo.write('Papai vadiou, mamãe dançou, por isso eu aqui estou.\n')
novo_arquivo.close()

