import os
import arquivo as arq
import util
import voto
from time import sleep

# Criação de CONSTANTES
PATH_REL = 'projeto_final'
PATH_ABS = '/home/asaito2001/repos/python3/PJC/projeto_final'
BASE_ELEITORES = os.path.join(PATH_REL, 'dados', 'base_eleitores.csv')
CERTIDAO = os.path.join(PATH_REL, 'dados', 'certidao.html')

# Verificar existencia de arquivos
if not arq.existe_arquivo(BASE_ELEITORES):
    arq.criar_base_eleitores(BASE_ELEITORES)
    print('Arquivo base eleitores criado com sucesso!!')
else:
    print('Base de dados encontrada!')


# Programa principal
menu = ('Cadastro', 'Validação', 'Emissão Certidão', 'Sair do Sistema')
dados_busca = []
while True:
    opcao = util.menu(menu, 'QUITAÇÃO ELEITORAL', 40)
    if opcao == 1:
        dados = arq.cadastrar_eleitor()
        if arq.gravar_eleitor(dados, BASE_ELEITORES):
            print('Gravado com sucesso!')
        else:
            print('Não foi possível cadastrar o eleitor')
        sleep(1.5)
    elif opcao == 2:
        dados_busca = arq.buscar_eleitor(arq.solicitar_dados_busca(), BASE_ELEITORES)
        if voto.validar_eleitor(dados_busca):
            pass
            sleep(1.5)
        else:
            pass
            sleep(1.5)
    elif opcao == 3:
        if dados_busca:
            arq.emitir_certificado(dados_busca, CERTIDAO)
        else:
            print('Favor validar antes!!')
    else:
        util.titulo('Saída do Sistema >>> Até breve!')
        break